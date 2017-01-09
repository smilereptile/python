# -*-coding:Latin-1 -*

# https://openclassrooms.com/courses/apprenez-a-programmer-en-python/les-listes-et-tuples-2-2


ma_chaine = "Bonjour à tous"
list_from_string = ma_chaine.split()

print(ma_chaine, list_from_string)

ma_liste = ['Bonjour', 'à', 'tous']
string_from_list = " ".join(ma_liste)

print(ma_liste, string_from_list)


def afficher_flottant(flottant):
    if type(flottant) is not float:
        raise TypeError("Le paramètre attendu doit être un float")

    # Remplace le point du flottant par une virgule
    str1 = str(flottant).replace(".", ",")

    # Remplace le point par une virgule d'une autre manière
    str2 = ",".join(str(flottant).split("."))

    # Solution
    partie_entiere, partie_flottante = str(flottant).split(".")
    return ",".join([partie_entiere, partie_flottante[:3]])
    # print(str1)
    # print(str2)


mon_float = 2.66148
mon_float_res = afficher_flottant(mon_float)
print(mon_float, mon_float_res)

a = [0, 5, 10, 17, 23, 4, 1]

b = [elt * elt for elt in a]

c = [elt - 178 for elt in b if elt > 178]

print(a, b, c)

inventaire = [("pommes", 22), ("melons",4), ("poires",18), ("fraises", 76), ("prunes", 51), ]
print(inventaire)
r_inventaire = [(nb, fruit) for (fruit, nb) in inventaire]
r_inventaire = [(nb, fruit) for (fruit, nb) in r_inventaire]
print(sorted(r_inventaire, reverse=True))

