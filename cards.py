import random


suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']# Define suits and ranks
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [(rank, suit) for suit in suits for rank in ranks]# Create a deck of cards

random.shuffle(deck)# Shuffle the deck

if len(deck)==0:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']# Define suits and ranks
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [(rank, suit) for suit in suits for rank in ranks]# Create a deck of cards

random.shuffle(deck)# Shuffle the deck
    

    

    

    
    