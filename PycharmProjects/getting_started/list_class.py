# -*-coding:Latin-1 -*

# List (mutable)
ma_liste = [1, 2, 3, 4, 5]
ma_liste[3] = "R"
ma_liste.append([])
ma_liste.insert(2, 23.1)
liste2 = ["la suite"]
ma_liste.extend(liste2)
ma_liste += ["Point final"]

print(ma_liste)

del ma_liste[0]

# la méthode remove ne supprime la première occurrence seulement
ma_liste.remove(23.1)

for elt in ma_liste:
    print(elt)

for elt in enumerate(ma_liste):
    print(elt)


# Tuple (non mutable). Pas de méthode pour
tuple1 = ()
tuple1 = (1,)
tuple1, what = (1, 2, tuple1), 5


print(tuple, what)

