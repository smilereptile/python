annee = input("""Saisir une annee :""")

annee = int(annee)

if (annee % 400 == 0) or (annee % 4 == 0 and annee % 100 != 0):
    print(annee, """bissextile""")
else:
    print(annee, """n'est pas bissextile""")
