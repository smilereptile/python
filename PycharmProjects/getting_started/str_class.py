# -*-coding:Latin-1 -*

# https://openclassrooms.com/courses/apprenez-a-programmer-en-python/notre-premier-objet-les-chaines-de-caracteres

minuscules = "une chaine en minuscules"
minuscules.upper().center(35).strip().capitalize().lower()

prenom = "Mat"
nom = "Mat"
age = 37
print(
    "Je m'appelle {0} {1}, j'ai {2} ans"
    .format(prenom, nom, age))

# ou

print(
    "Je m'appelle {} {}, j'ai {} ans"
    .format(prenom, nom, age))

# ou
# formatage d'une adresse

adresse = """

{no_rue}, {nom_rue}

 {code_postal} {nom_ville} ({pays})

""".format(no_rue=5, nom_rue="rue des Postes", code_postal=75003, nom_ville="Paris", pays="France")

print(adresse)

chaine = "Salut les gens !"

i = 0
while i < len(chaine):
    print(chaine[i])
    i += 1


# changer un caractère ou un ensemble de caractère d'un str
# ne fonctionne pas
# chaine[6] = "h"

# pour que cela marche, il faut faire des selections
chaine = chaine[0:6] + "h" + chaine[7:]
print(chaine)
