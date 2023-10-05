# Praeses Blackjack
 BlackJack Game in Python

Play the BlackJack Card game with one or more players.

## Description
The Blackjack game program consists of one or more players and a dealer.
The player attempts to beat the dealer by getting a count as close to 21 as possible, without going over 21.
An in-depth paragraph about your project and overview of use.

## Getting Started

### Dependencies
python3.11.5 needed before installing program.

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10 and above

### Installing

* How/where to download your program
  https://www.python.org/downloads/
 To install Python on Windows, download the latest version of Python from the Python website, then run the installer. Ensure that you add Python to the PATH when presented with the option.

* Any modifications needed to be made to files/folders
  NA
  
### Executing program

* How to run the program
How to run the program
- Open a command line console
- Go to the path where the source is copied
- Type PlayBlackJack.py
- Hit enter

* Step-by-step bullets
Game Play: Steps to play a hand
Create a deck of 52 cards
Shuffle the deck
Ask the Player if they are over 18 years
Ask the Player for the value of Ace to be used in that game/hand
Ask the Player for their bet
Make sure that the Player’s bet does not exceed their available chips
Deal two cards to the Dealer and two cards to the Player
Show only one of the Dealer’s cards, the other remains hidden
Show both of the Player’s cards
Ask the Player if they wish to Hit, and take another card
If the Player’s hand doesn’t Bust (go over 21), ask if they’d like to Hit again.
If a Player Stands, play the Dealer’s hand. The dealer will always Hit until the Dealer’s value meets or exceeds 17
Determine the winner and adjust the Player’s chips accordingly
Ask the Player if they’d like to play again

The End Game
When the dealer’s score is either 17 or more, we move onto the End Game, which involves comparing of values and nominating the winner of the game. There can be a few scenarios possible:

The Dealer Busts – The dealer’s score exceeds 21.
The Dealer has Blackjack – The dealer has an exact score of 21.
The Player Busts – The player’s score exceeds 21.
The Player has Blackjack – The player has an exact score of 21.
A Tie Game – Both the player and the dealer has equal score.
The Player Wins – The player’s score is more than that of the dealer.
The Dealer Wins – The dealer’s score is more than that of the player.
We check for each of the above possibilities and declare the winner.

Classes used in the code:
- Card Class: Has two attributes: suit and rank. Returns a string like “Two of Hearts”
- Deck Class: Instantiate all 52 unique card objects and add them to the list. Has methods to shuffle the deck, and to deal out cards during gameplay.
- Hand Class: Holds Card objects dealt from the Deck, the Hand class is used to calculate the value of those cards using the values dictionary defined in Deck. Has method to     	      adjust the value of Aces when appropriate.
- Chips Class: Keeps track of a Player’s starting chips, bets, and ongoing winnings.

Functions used in the code:
- take_bet: Store the integer value of chips that is within the Player's betting limit.
- hit:  Called during gameplay anytime a Player requests a hit or a Dealer’s hand is less than 17. Deck and Hand objects are arguments.	It will deal one card off the deck and 	add it to the Hand. It has the ability to check for aces in the event that a player’s hand exceeds 21, if the player does not choose a value for Aces.
- hit_or_stand: Prompt the user for hit or stand. If the Player Hits, employ the hit() function. If the Player Stands, set the playing variable to False.
- show_some: The Dealer’s first card is hidden and all of Player’s cards are visible in the first hand.
- show_all: All of Dealer's and Player’s cards are visible at the last hand. Also shows each hand’s total value.
- player_busts: When the Player's total value exceeds 21.
- player_wins: When the Player's total value is more than the Dealer's.
- dealer_busts: When the Dealer's total value exceeds 21.
- dealer_wins: When the Dealer's total value is more than the Player's.
- push: When the Dealer's and the Player's total value is the same aka a tie.
- sortdeck: This method is used to sort the cards after shuffle and combine the cards in the deck based on the suit and color.


Adiditional features:
Prompt for age to validate if eligible to play BlackJack.
Prompt for value of Ace.
Prompt for Chips and check it does not exceed the maximum limit and is greater than 0.
If Ace value is not selected it defaults to adjust_for_aces method that decreases the number of aces to make an adjustment to stay under 21.


## Help

Any advise for common problems or issues.
Hit ctrl+c to end the program.
Run the program again.

command to run if program contains helper info
NA

## Authors
Devamani Francis

Contributors names and contact info
NA

## Version History
Versio 1.0 Intitial Release

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details
NA

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-gameplaydetails](https://bicyclecards.com/how-to-play/blackjack/)
* [simple-readme](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc#file-readme-template-md)

