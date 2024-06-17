from cards import *

def deal_cards(deck):#A function of dealing the cards to the players
    player_hand = []#a list that holds the player's cards
    computer_hand = []#a list that holds the computer's cards
    for i in range(4): # the loop goes thru the underlying code causing it to run the specified number of times hence ensuring that the list has the specified number of cards.
      player_hand.append(deck.pop())# adds the cards from the deck into the list.
      computer_hand.append(deck.pop())# adds the cards from the deck into the list.
    return player_hand,computer_hand
  
    
player_hand,computer_hand = deal_cards(deck)#calling the function



