# -*-coding:Latin-1 -*

annee = input("""Saisir une ann�e :""")
# annee2 = int(annee)

try:
    annee = int(annee)
except ValueError:
    print("Valeur pour annee incompatible avec une annee")
except TypeError:
    print("Type incompatible avec une annee")
except NameError:
    print("Variable non definie")
except ZeroDivisionError:
    print("Division par z�ro")
else: # on peut placer ici le reste du code qui ne craint pas d'exception, comme le print ou le return
    print("""L'ann�e saisie est """, annee)
finally: # est ex�cut� syst�matiquement, m�me s'il y a un return, break ou autre instruction dans un des blocs pr�c�dents
    print("""Ce message s'affiche syst�matiquement !!!""")
