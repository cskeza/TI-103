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

print(compte([2,4,5]))

print(sum([2,4,5]))