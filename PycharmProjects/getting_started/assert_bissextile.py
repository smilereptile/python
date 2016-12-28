# -*-coding:UTF8 *-

annee = input("Saisir une année : ")

try:
    annee = int(annee)
    assert annee > 0
except ValueError:
    print("Valeur pour annee incompatible avec une annee")
except AssertionError:
    print("""La valeur de l'année ne peut être négative : """, annee)
