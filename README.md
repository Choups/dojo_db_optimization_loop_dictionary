# Optimiser ses requêtes SQL grâçe aux dictionnaires Python

L'objectif de cette pratique est d'éviter d'effectuer des requêtes SQL au sein d'une boucle. Il est préférable d'effectuer une requête qui remplit un dictionnaire python et de boucler sur celui-ci via sa clé pour un gain de temps considérable.

## 1 requête dans 1 boucle qui itère 1000 fois
temps d'execution: TRES LONG

## 1 requête + 1 boucle qui itère 1000 fois sur 1 dictionnaire 
temps d'execution: TRES RAPIDE

Voir le script python optidbdict.py et l'éxecuter pour mieux comprendre.
