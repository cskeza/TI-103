l = [1, 2, 4]

print(l[1:])
print(l)
print(l[0])

l = list(range(0, 9))
print(l)

l.append(20)
print(l)
l.pop()

print(l.pop())

l.insert(0, "Christa")
print(l)

l.pop(0)
print(l)


for i in l:
    print(i)


"Une liste qui retourne la somme des elements d'une liste"


def compte(l):
    somme=0

    for i in l:
        somme=somme+i

    return somme
print(compte([2,4,5,6]))



