from hand import *
from cards import deck
import random

played=[random.choice(deck)]

def playermoves(player_hand):
   
    print(f"Your hand: {player_hand}")
    print(f"Played Cards: {played}")
    
    rank = input("Enter the card rank: ").strip()
    suit = input("Enter the card suit: ").strip()
    
    
    play = (rank, suit)
   
    if play in player_hand:
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
        print(f"Card {play} not in hand, play something else")
        playermoves(player_hand)

player_hand = playermoves(player_hand)  


