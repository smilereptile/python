# -*-coding:Latin-1 -*


def table(nb, max=10):
    """Fonction qui calcule des tables de multiplication
    de nb de 0 jusqu'à max"""
    i = 0
    while i <= max:
        print(nb, " *", i, " = ", nb * i)
        i += 1
