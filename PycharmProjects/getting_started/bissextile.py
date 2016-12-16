annee = input("""Saisir une annee :""")

annee = int(annee)

bissextile = False

if annee % 400 == 0:
    bissextile = True
elif annee % 100 == 0:
    bissextile = False
elif annee % 4 == 0:
    bissextile = True
else:
    bissextile = False

if bissextile:
    print(annee, """bissextile""")
else:
    print(annee, """n'est pas bissextile""")
