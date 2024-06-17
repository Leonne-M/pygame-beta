from hand import *
from cards import deck
import random

played=[random.choice(newdeck)]


def playermoves(player_hand):
   if played[-1][0]in ['8', 'King', 'Jack', 'Queen']:
    return print("Your turn has been skipped")
   else:
    print(f"Your hand: {player_hand}")
    print(computer_hand)
    print(f"Played Cards: {played}")
    
    rank = input("Enter the card rank: ").capitalize().strip()
    suit = input("Enter the card suit: ").capitalize().strip()
    
    
    play = (rank, suit)
   
    if play in player_hand and (play[0] in played[-1][0] or play[1] in played[-1][1]):
        if played[-1][0]=='3' or played[-1][0]== '2' and play[0]!='Ace':  
             for i in range(int(played[-1][0])):
               player_hand.append(deck.pop())
               return
        played.append(play)
        if play[0]=="Ace":
           newsuit=input("Enter the new card suit: ")
           played[-1]=(played[-1][0],newsuit)
           print(f"The game was changed to {newsuit}")
        player_hand.remove(play)
    elif rank=="Pick":
        player_hand.append(deck.pop())
        print("You picked!!")
        return
    else:
        print(f"Card {play} is not playable ")
        playermoves(player_hand)
playermoves(player_hand)  


