

class MerkleTrie:
    def __init__(self, letter):
        self.letter= letter
        self.children = []

    def __contains__(self, item):
        for c in self.children:
            if c.letter == item:
               return True

        return False
    def __eq__(self, other):
        if other == self.letter:
            return True
        return False

    def __len__(self):
        return len(self.children)



    def is_leaf(self):
        if not self.children:
            return True

        else:
            return False

    def add(self, letter):
        for child in self.children:
            if child.letter == letter:
                return child
      #condition ou la lettre n'existe pas, donc on en cree une nvlle et on la retourne
        obj = MerkleTrie(letter)
        self.children.append(obj)
        return obj

    def dump(self, racine):
        if self.is_leaf():
            print(racine + self.letter)

        else:
            for child in self.children:
                child.dump(racine + self.letter)

#. Ajouter des mots entiers

def add_new_word(root, new_word):
    """
    add_new_word(p, "Rubens")
    => var = r.add("u")
    => var = var.add("b")
       var.add("e")
    """
    if new_word[0] == root:
        var = root
        for l in new_word[1:]:
            var = var.add(l.lower())



    else:
         return

dictionary= ["romane", "romanus"]

r= MerkleTrie("r")
for word in dictionary:
    add_new_word(r, word)

r.dump("")
#.Verifier qu'une lettre existe ds les enfants d'un noeud




r = MerkleTrie("r")
r.add("o")

if "o" in r:
    print(":)")
else:
    print(":(")

if "r" == r:
    print(":)")

else:
    print(":(")
print(r.letter)
print(r.is_leaf())

print(f"{r.letter} has {len(r)} children nodes")
r.dump("")