from hand import *
from cards import deck
import random
from playermoves import played



def compmoves(computer_hand):
  print(f"Comp hand: {computer_hand}")
  
  can_be_played=[]
  if played[-1][0] in ['8', 'King', 'Jack', 'Queen']:
    return
  elif played[-1][0]=='3' or played[-1][0]== '2':
   for i in range(int(played[-1][0])):
    computer_hand.append(deck.pop())
   return
  else:
   for i in range(len(computer_hand)):
    if computer_hand[i][0] in played[-1][0] or computer_hand[i][1] in played[-1][1]:
       can_be_played.append(computer_hand[i])

   if not can_be_played:
    computer_hand.append(deck.pop())
    return print("computer picked!!")
  
   playing= random.choice(can_be_played)
   rank,suit=playing
   play = (rank, suit)
   played.append(play)
   computer_hand.remove(play)
   print(can_be_played)
   print(played)
   return print("computer played")
compmoves(computer_hand)
   