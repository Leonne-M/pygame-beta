from hand import *
from cards import deck
import random

played=[random.choice(newdeck)]


def playermoves(player_hand):
   
        print(f"Your hand: {player_hand}")
        print(f"Computer's hand: {computer_hand}")
        print(f"Played Cards: {played}")

        rank = input("Enter the card rank: ").capitalize().strip()
        suit = input("Enter the card suit: ").capitalize().strip()

        play = (rank, suit)

        if play in player_hand and (play[0] == played[-1][0] or play[1] == played[-1][1]):
            if (played[-1][0] in ['3', '2'] and play[0] != 'Ace'): 
                for _ in range(int(played[-1][0])): 
                      player_hand.append(deck.pop())
                return
            played.append(play)
            player_hand.remove(play)
            if play[0] == "Ace":
                newsuit = input("Enter the new card suit: ").capitalize().strip()
                played[-1] = (played[-1][0], newsuit)
                print(f"The game was changed to {newsuit}")
            if play[0] in ['8', 'King', 'Jack', 'Queen']:
                return playermoves(player_hand)
            
        elif rank() == "Pick": 
            player_hand.append(deck.pop())
            print("You picked a card!")
            
        else:
            print(f"Card {play} is not playable. Please try again.")
            playermoves(player_hand)



