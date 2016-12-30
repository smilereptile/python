# -*-coding:Latin-1 -*

# fonction random
from random import randrange
# Arrondi
from math import ceil

money = 50
output = """InitMe"""
cpt = 0

def color_black(chance):  # fonction qui teste la couleur. black est pair, red est impair
    if chance % 2 == 0:
        return True
    else:
        return False

while money > 0:
    bet = randrange(1, 6)
    print("""Money bet : """, bet)
    myguess = randrange(50)
    print("""My guess : """, myguess)
    case = randrange(50)
    print("""Bank Case:""",case)
    if myguess == case:
        money += ceil(3 * bet)
        output = """Bet win, found case. Money = """
    elif color_black(myguess) == color_black(case):
        money += ceil(bet/2)
        output = """Bet win, found color. Money = """
    else:
        money -= bet
        print("""Bet lost. Money = """, money)

    print(output,money)
    cpt += 1


print("""You leave with $""", money)
print("""You played """, cpt, """times""")
