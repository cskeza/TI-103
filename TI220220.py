l=[1, "4",6,9]

print(l[2])

print([])

ll=list(range(1,9))
print(ll)

l.append(5)  #ajouter un element
print(l)

print(len(l))  #demander la liste d'elts
l.pop()  #enlever un elt
print(l)

l.insert(0, "Toto")
print(l)


for i in l:
    print(i)

"Une fonction qui accepte en parametre une liste et qui retourne la somme des elts de la liste"

def compte (l):
    somme = 0
    for i in l:
        somme = somme + i

    return somme

"""
Une fonction qui donne les x premiers nbres carrees et retoune une liste,
ou x est un parametre
"""

def puissances(x):
    l=[]

    for i in range (1, x+1):
        l.append(i**3)

    return l


#print(compte([2,4,5]))

#print(sum([2,4,5]))

print(puissances(12))

l1= [1,2,4]
l2=[3,6]
print (l1+l2)

"""
Fonction qui dit si un elt est ds la liste
"""
def est_dans_la_liste(l, elem):

    if elem in l:
        return True
    else:
        return False
"Fonction qui donne en retour le nbre d'occurence ds la liste"

def compte_ds_liste(l, elem):
    i=0

    while elem in l:
        i +=1
        l.remove(elem)

    return i
