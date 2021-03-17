

class MerkleTrie:
    def __init__(self, letter):
        self.letter= letter
        self.children = []

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
                return

        self.children.append(MerkleTrie(letter))

    def dump(self, racine):
        if self.is_leaf():
            print(racine + self.letter)

        else:
            for child in self.children:
                child.dump(racine + self.letter)


r = MerkleTrie("r")
r.add("o")


print(r.letter)
print(r.is_leaf())

print(f"{r.letter} has {len(r)} children nodes")
(r.dump(""))