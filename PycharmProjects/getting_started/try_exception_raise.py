# -*-coding:UTF8 *-

annee = input("Saisir une année : ")

try:
    annee = int(annee)
    if annee <= 0:
        raise ValueError("""L'année ne peut être nulle ou négative""")
except ValueError:
    print("Valeur pour annee incompatible avec une annee")
