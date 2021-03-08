
class Etudiant:
    def __init__(self, nom, prenom, numero, adresse):
        self.nom = nom
        self.prenom = prenom
        self.numero = numero
        self.adresse = adresse

jean_dupont = Etudiant("dupont", "jean", 1, "N/A")
jeanne_dupont = Etudiant("dupont", "jeanne", 2, "N/A")
Christa_Keza = Etudiant("Keza", "Christa", 3, "N/A")

print(jean_dupont.nom)
print(Christa_Keza.nom)