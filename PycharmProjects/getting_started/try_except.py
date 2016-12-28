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
else:  # on peut placer ici le reste du code qui ne craint pas d'exception, comme le print ou le return. Attention le
    #  else n'est pas ex�cut� s'il y a une exception non g�r�e plus haut dans le code
    print("""L'ann�e saisie est """, annee)
finally:  # est ex�cut� syst�matiquement, m�me s'il y a un return, break ou autre instruction dans un des blocs pr�c�dents
    print("""Ce message s'affiche syst�matiquement !!!""")
    pass  # cela signifie qu'on ne fait rien. A eviter
