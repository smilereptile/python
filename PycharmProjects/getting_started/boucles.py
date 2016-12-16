cpt = 0
start = 0

while cpt < 10:
    if start % 7 == 0 and start % 17 == 0:
        print("""Multiple de 7 et 17 :""", start)
        cpt += 1
    start += 1

chaine = """Salut les gens!"""
for lettre in chaine:
    print(lettre)
