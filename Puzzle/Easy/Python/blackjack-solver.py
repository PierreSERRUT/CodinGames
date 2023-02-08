# blackjack-solver
# python

import sys
import math

ten_points_cards=['K','Q','J','10']

def calcul_tot(c):
    t=0
    if len(c) == 2 and ((c[0] == 'A' and c[1] in ten_points_cards) or (c[1] == 'A' and c[0] in ten_points_cards)):
        return 'Blackjack!'

    for i in reversed(c):
        if i in ten_points_cards:
            t+=10
        elif i == 'A':
            if t+11 > 21:
                t+=1
            else:
                t+=11
        else:
            t+=int(i)
    return t


bank_cards = input().split()
player_cards = input().split()

# print(bank_cards, file=sys.stderr, flush=True)
# print(player_cards, file=sys.stderr, flush=True)

tot_play=calcul_tot(player_cards)
tot_bank=calcul_tot(bank_cards)

if tot_bank == 'Blackjack!' and tot_play != 'Blackjack!':
    print("Bank")

elif tot_play == 'Blackjack!' and tot_bank != 'Blackjack!':
    print('Blackjack!')

elif tot_bank == tot_play and (tot_play == 'Blackjack!' or tot_play <22):
    print("Draw")
elif tot_bank > tot_play and tot_bank <22 or tot_play > 22:
    print("Bank")
else:
    print("Player")
