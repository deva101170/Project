#! /usr/bin/python

''' 
BlackJack card game play

'''

import random
import sys

#suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
         
playing = True
playerval = 21
dealerval= 17  

#creating card class#

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

#creating Deck, shuffle function and single dealing#

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list#
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
        
    def __str__(self):
        deck_comp = '' #starting competition deck empty#
        for card in self.deck:
            deck_comp += '\n' + card.__str__() #add each card object
        return deck_comp        
            
    def shuffle(self):
        #print('shuffle deck')
        random.shuffle(self.deck)
        
    def sortdeck(self):
        deck_spades = ''
        deck_clubs = ''
        deck_hearts = ''
        deck_diamonds = ''
        deck_comp_sort = ''
        print('\nSort cards in deck')
        for card in self.deck:
            if card.suit == "Spades":
                deck_spades += '\n' + card.__str__() #add Spades        
            if card.suit == "Clubs":
                deck_clubs += '\n' + card.__str__() #add Clubs
            if card.suit == "Hearts":
                deck_hearts += '\n' + card.__str__() #add Hearts
            if card.suit == "Diamonds":
                deck_diamonds += '\n' + card.__str__() #add Diamonds
 
        deck_comp_sort = deck_spades + deck_clubs + deck_hearts + deck_diamonds
        print(deck_comp_sort)            
      
        
      
    def deal(self):
        #print('deal deck')
        single_card = self.deck.pop()
        #print(single_card)
        return single_card

#creating a hand#

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > playerval and self.aces:
            #print(self.value) 
            self.value -= 10
            self.aces -= 1
            
#creating Chips balance for competitor#            

class Chips:
    
    def __init__(self):
        self.total = 500  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -+ self.bet

''' ************************************************************************************************************************************** '''
        
#Taking bets#

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet?  '))
        except ValueError:
            print("Sorry, a bet must be an integer!")
        else:
            if chips.bet > chips.total:
                print('Sorry, your bet cannot exceed {} '.format(chips.total))
                continue
            if chips.bet < 2:
                print('Sorry, enter a value greater than 1 ')
            else:
                break      

# taking hits#

def hit(deck,hand):
    hand.add_card(deck.deal())
    if aceval == 0:
    	hand.adjust_for_ace()

#player to take hits or stand#

def hit_or_stand(deck,hand):
    global playing
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's'")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, invalid entry. Please try again.")
            continue
        break

#functions to display cards#

def show_some(player,dealer):
    print("\nDealer's Hand")
    print("<card hidden>")
    print(' ', dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep='\n')
    print("")
        
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep="\n")
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep='\n')
    print("Player's Hand = ", player.value)

#functions to handle game scenarios#

def player_busts(player,dealer,chips):
    print("\nPlayer busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("\nPlayer wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("\nDealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("\nDealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("\nDealer and Player tie! It's a push.")  

#functions to set up game scenarios#

def validateage():
    ValidateAge = input('Are you 18 years or older? [Please enter "y" for Yes and "n" for No]: ') 
    if ValidateAge == "y":
       status="Eligible"
    elif ValidateAge == "n":
    	 status="Not Eligible"
    	 print("You are ",status," to Play.")
    	 sys.exit(0)
    else:
    	 print("Sorry invalid entry. Please try again")

def acevalue():
    global aceval
    while True:
        try:
            aceval = int(input('What do you want the value of ACE to be? [Enter 1 OR 11.] [Enter 0 if you want the the game to automatically adjust the value]: '))
        except ValueError:
            print("Sorry, Input must be an integer!\n")
        else:
            if aceval != 11 and aceval != 0 and aceval != 1:
                print('Please enter a valid val for Ace') 
                continue
            elif aceval > 0:
                values['Ace'] = aceval
            break
            

''' ************************************************************************************************************************************** '''

#NOW FOR THE GAME

#Verify age to play
validateage()

# Print an opening statement
print("Let's play Blackjack!\n")

while True:

    # Prompt for value of ACE and append to dict
    aceval = 11
    acevalue()

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    print(deck)
    
    deck.sortdeck()
    
   
    # # The second parameter is the input iterable
    # # The filter() applies the lambda to the iterable
    # # and only returns all matches where the lambda evaluates
    # # to true
    # sortdeck = filter(lambda a: 'Spades' in a, deck) 
    # # Convert the filter object to list
    # print(list(sortdeck))
    
    
    # print('Sort cards and print')     
    # showdecksort = deck.sortdeck()
    # for i in showdecksort:
        # print(f' Sorted card by black and red: {i.suit} {i.rank}' )
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # Set up the Player's chips
    player_chips = Chips()
        
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand) 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value >playerval:
            player_busts(player_hand, dealer_hand, player_chips)
            # Show all cards
            show_all(player_hand,dealer_hand)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= playerval:
        
        while dealer_hand.value < dealerval:
            hit(deck, dealer_hand)
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > playerval:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)
        
    
    # Inform Player of their chips total
    print("\nPlayers winnings stand at", player_chips.total, "\n")
    
    # Ask to play again
    new_game = input("would you like to play again? Enter 'y' or 'n'")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thanks for playing! ')
        break