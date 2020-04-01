import random
import time

########## SETUP ############
# Simulation du temps de réponse des requêtes SQL en secondes:
fake_time_for_filtered_db_query = 0.15
fake_time_for_global_db_query = 0.20


######################################################
# CAS 1: une requête sur chaque élément de la liste: #
######################################################
print('-------------- Début du cas 1 ---------------')

list_of_datas = []
time_cas_1 = 0

for loop in range(30):
  # simulation de notre requête SQL individuelle ici qui ajoute la value à notre list
  time_cas_1 += fake_time_for_filtered_db_query
  time.sleep(fake_time_for_filtered_db_query)
  result = random.randrange (1,2000,1)
  print('requête filtrée n°', loop + 1, ' terminée ------> résultat:',result)
  list_of_datas.append({'id':loop,'value':random.randrange (1,2000,1)})


print('TOTAL :',sum(data['value'] for data in list_of_datas))
print('TEMPS:',time_cas_1, 'secondes')


#######################################################################
# CAS 2: une requête qui remplit un dictionnaire sur lequel on itère: #
#######################################################################
print('-------------- Début du cas 2 ---------------')

list_of_datas_2 = []
time_cas_2 = 0

# simulation de notre requête SQL groupée ici
time_cas_2 += fake_time_for_global_db_query
time.sleep(fake_time_for_global_db_query)
result = list_of_datas
print('requête globale terminée ------> résultat:', result)

# attribution de chaque objet dans un dictionnaire: 
my_dictionary = {data['id']: data['value'] for data in result}

for loop in range(30):
  list_of_datas_2.append(my_dictionary.get(loop, 0))

print('TOTAL :',sum(list_of_datas_2))
print('TEMPS:',time_cas_2, 'secondes')
print('Le cas 2 est',round(time_cas_1/time_cas_2, 2),'fois plus rapide')
