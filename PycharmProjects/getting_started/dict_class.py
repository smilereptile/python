# -*-coding:Latin-1 -*
# https://openclassrooms.com/courses/apprenez-a-programmer-en-python/les-dictionnaires-2

mon_dico = dict()
mon_dico["prenom"] = "mat"
mon_prenom = mon_dico["prenom"]
mon_dico["age"] = 37
mon_dico2 = {"chemise": 3, "pantalon": 5, "chaussettes": 11}

# how to remove
# del mon_dico2["pantalon"]
# mon_dico2.pop("chaussettes")


def parcours(dico):
    for cle, valeur in dico.items():
          print(format(cle, valeur))

for cle, valeur in mon_dico2.items():
    mkey = str(cle)
    mvalue = str(valeur)
    print(cle, valeur)

print("{}, {}".format(cle, valeur))


# parcours(mon_dico2)
