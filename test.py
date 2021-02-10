"""
1.Vous chisisssez un nombre de 1 a 1000 et vous l'assignez a une variable
2.Puis, tant qu'un utilisateur ne frappe pas la touche "q", vous lui demandez de choisir un nombre
3.Si le nombre est inferieur a la variable assignee, vous lui dites "Plus grand"
4.Si le nombre est superieur a la variable assignee, vous lui dites "Plus petit"
5.L'utilisateur gagne s'il trouve la bonne valeur.
6.Vous devez tester que le nombre entre est correct. Par exemple, retournez une erreur si ce que vous trouvez n'est pas un nombre, ou n'est pas compris entre 1 et 1000
"""

import random

import test_import

a= random.randint(1, 1000)

print(test_import.fibonacci(test_import.ma_variable))

while True:

    entree= input("Entrez un nombre entre 1 et 1000 puis entree, faites 'q' puis entree pour quitter")

    if entree=='q':
        break

    elif not entree.isnumeric():
        print("Vous devez entrer un nombre entier")
        continue

    elif int(entree)<=0:
        print("Entrez un nombre plus grand ou egal a 1.")
        continue

    elif int(entree)>1000:
        print("Entrez un nombre plus petit ou egal a 1000.")
        continue

    elif int(entree)<a:
        print("Plus grand.")
        continue

    elif int(entree)>a:
        print("Plus petit.")
        continue

    elif int(entree)==a:
        print("GAGNE!!!!!")
        break