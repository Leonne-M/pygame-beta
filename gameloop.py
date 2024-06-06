from playermoves import playermoves
from comp import compmoves
from hand import *

def gameloop(player_hand, computer_hand):
    while True:
        if len(player_hand) == 0:
            print("Player wins!")
            break
        elif len(computer_hand) == 0:
            print("You lose!")
            break
        playermoves(player_hand)
        
        if len(player_hand) == 0:
            print("Player wins!")
            break
        elif len(computer_hand) == 0:
            print("You lose!")
            break
  
        compmoves(computer_hand)
    
gameloop(player_hand, computer_hand)
