def table_nb(nb, max=10):
    """Fonction qui calcule des tables de multiplication
    de nb de 0 jusqu'à max"""
    i = 0
    while i <= max:
        print(nb, " *", i, " = ", nb * i)
        i += 1

table_nb(9)
table_nb(9, 11)


def fonc(a=1, b=2, c=3, d=4, e=5):
    print("a = ", a, "b = ", b, "c = ", c, "d = ", d, "e = ", e)


fonc()
fonc(11)
fonc(d=14, b=12)

def carre(valeur):
    """Calcule le carre d'un nombre"""
    return valeur * valeur

print("carre = ", carre(7))
