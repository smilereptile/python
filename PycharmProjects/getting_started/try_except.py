# -*-coding:Latin-1 -*

annee = input("""Saisir une année :""")
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
    print("Division par zéro")
else: # on peut placer ici le reste du code qui ne craint pas d'exception, comme le print ou le return
    print("""L'année saisie est """, annee)
finally: # est exécuté systématiquement, même s'il y a un return, break ou autre instruction dans un des blocs précédents
    print("""Ce message s'affiche systématiquement !!!""")
