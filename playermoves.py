from hand import *
from cards import deck
import random

played=[random.choice(newdeck)]


def playermoves(player_hand):
   if played[0] in ['8', 'King', 'Jack', 'Queen']:
    return print("Your turn has been skipped")
   else:
    print(f"Your hand: {player_hand}")
    print(f"Played Cards: {played}")
    
    rank = input("Enter the card rank: ").strip()
    suit = input("Enter the card suit: ").strip()
    
    
    play = (rank, suit)
   
    if play in player_hand and (play[0] in played[-1][0] or play[1] in played[-1][1]):
        if played[-1][0]=='3' or played[-1][0]== '2':
            for i in range(int(played[-1][0])):
              player_hand.append(deck.pop())
              return
        played.append(play)
        player_hand.remove(play)
        print(played)
        print(player_hand)
    elif rank=="Pick":
        player_hand.append(deck.pop())
        print(player_hand)
        print("You picked!!")
        return player_hand
    else:
        print(f"Card {play} is not playable ")
        playermoves(player_hand)

player_hand = playermoves(player_hand)  


