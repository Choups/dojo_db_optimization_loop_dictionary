# dojo_db_optimization_loop_dictionary

L'objectif de cette pratique est d'éviter d'effectuer des requêtes SQL au sein d'une boucle. Il est préférable d'effectuer une requête qui remplit un dictionnaire python et de boucler sur celui-ci via sa clé pour un gain de temps considérable.

## 1 requête dans 1 boucle qui itère 1000 fois (tps d'execution: <span style="color:red">TRES LONG</span>)
exemple:

`for kb_ref in kb_references: item = {'id': kb_ref.reference.code, 'card_in_stock': None } nb_card_in_stock = db.query(func.count(KanbanCard.uniqid))\ .join(KanbanReference)\ .join(Reference)\ .filter(KanbanCard.last_workstation == Workstation.get_from_name('En Stock', db))\ .filter(Reference.code == kb_ref.reference.code)\ .group_by(Reference.code)\ .first() item['card_in_stock'] = nb_card_in_stock`

## 1 requête + 1 boucle qui itère 1000 fois sur 1 dictionaire (tps d'execution: <span style="color:green">TRES RAPIDE</span>)
exemple:

`q_nb_card_in_stock = db.query(func.count(KanbanCard.uniqid).label('count'), (KanbanReference.uniqid).label('refid'))\ .join(KanbanReference)\ .join(Reference)\ .filter(KanbanCard.last_workstation == Workstation.get_from_name('En Stock', db))\ .filter(KanbanReference.loop == LoopType('loop_supply_external'))\ .group_by(KanbanReference.uniqid)\ .all() scans_nb_card_in_stock = {card.refid: card.count for card in q_nb_card_in_stock} for kb_ref in kb_references: item = {'id': kb_ref.reference.code, 'card_in_stock': scans_nb_card_in_stock.get(kb_ref.uniqid, 0) }`

