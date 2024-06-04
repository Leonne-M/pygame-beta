import random

# Define suits and ranks
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Create a deck of cards
deck = [(rank, suit) for suit in suits for rank in ranks]

# Shuffle the deck
random.shuffle(deck)

    

    

    
    