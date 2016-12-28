# -*-coding:Latin-1 -*

"""module multipli pour la fonction table"""
# https://openclassrooms.com/courses/apprenez-a-programmer-en-python/pas-a-pas-vers-la-modularite-2-2

import os

def table(nb, max=10):
    """Fonction qui calcule des tables de multiplication
    de nb de 0 jusqu'à max"""
    i = 0
    while i <= max:
        print(nb, " *", i, " = ", nb * i)
        i += 1

# test de la fonction table
if __name__ == "__main__":
    table(4)
    os.system("pause")

