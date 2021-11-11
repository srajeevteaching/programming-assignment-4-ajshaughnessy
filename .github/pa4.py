# Programmers: Aidan, Nicol
# Course: CS151, Dr. Rajeev
# Programming Assignment: 4
# Program Inputs: hit or stay
# Program Outputs: card and result

# Problem Create a program that lets the user play a simplified game of Blackjack, which is played between the user and
# an automated dealer as follows.

# The dealer shuffles a standard deck of 52 cards, draws two cards, and gives them to the user. The user can then choose
# to request another card from the dealer, adding it to their hand. The user can continue to request cards or choose to
# stop at any time. After each time the user requests a card, the program should output the cards in the
# player's updated hand and their total point value (see the function decomposition section below for how to calculate
# points). If, when receiving a new card, the total number of points in the hand goes over 21, the user loses. In this
# case, the dealer does not play.

# Once the user chooses to not draw any more cards, it is the dealer's turn to play, which is automated as follows. The
# dealer begins by drawing two cards. As long as the point value of the dealer's hand is less than 17, the dealer draws
# another card. When the point value of the hand is between 17 and 21 (inclusive), the dealer stops and the two hands
# (user's and dealer's) are compared. The player with the highest point value wins. If the point value of the
# dealer's hand goes over 21, the dealer has lost.

# Function decomposition Your program should have a function for at least each of the following tasks. You may have
# additional helper functions.

# A function that generates a shuffled deck of cards represented as a list. There are 52 cards in a deck: 13 clubs, 13
# diamonds, 13 hearts, and 13 spades. A card is represented as a string made up of a number between 1 and 13 and one
# character identifying the suit. For example, the string '8c' represents the 8 of clubs and '12d' represents the queen
# of diamonds. Use loops to generate the deck list in order and then use the random.shuffle function to randomly shuffle
# it. No user input or output should occur inside this function.

# A function which, given a string parameter representing a card (as described above), generates and returns a string
# with the card's name. For example, if the function receives '13h', the function should return 'King of Hearts'; if it
# receives '1s', the function should return 'Ace of Spades'; if it receives '3d' it should return '3 of Diamonds'. Use
# string indexing/slicing as needed to extract the number and suit. No user input or output should occur inside this
# function.

# A function which, given a list parameter representing a hand of cards, outputs the hand to the console, printing each
# card's name (as described above).

# A function which, given a list parameter representing a hand of cards, returns its total point value. A hand's point
# value is computed as the sum of point values of its cards. Each card's value is independent of its suit. An ace is
# worth 11 points. A face card (jack, queen, or king) is worth 10 points. All other cards are worth their value (for
# example, the 8 of clubs is worth 8 points). Use string indexing/slicing as needed to extract the number and suit. No
# user input or output should occur inside this function.

# A main function to drive the program and enable play.

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
playing = True

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self._deck = []
        for suit in suits:
            for rank in ranks:
                self._deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self._deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has' + deck_comp

    def shuffle(self):
        random.shuffle(self._deck)

    def deal(self):
        single_card = self._deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing
    while True:
        x = input("Hit or Stand? Enter 'h' or 's': ")
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print("Sorry, please try again.")
            continue
        break

def hide(player, dealer):
    print("Dealer's Hand")
    print(' ', dealer.cards[1])
    print("Player's Hand: ", *player.cards, sep='\n')

def show(player, dealer):
    print("Dealer's Hand:", *dealer.cards, sep="\n")
    print("Dealer's Hand =", dealer.value)
    print("Player's Hand: ", *player.cards, sep='\n')
    print("Player's Hand = ", player.value)

def player_busts(player, dealer):
    print("You Bust")

def player_wins(player, dealer):
    print("You win")

def dealer_busts(player, dealer):
    print("Dealer busts")

def dealer_wins(player, dealer):
    print("Dealer wins!")

def push(player, dealer):
    print("It's a push")

while True:
    print("Blackjack")
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    hide(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)
        hide(player_hand, dealer_hand)
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
        show(player_hand, dealer_hand)
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand)
        else:
            push(player_hand, dealer_hand)

    new_game = input("Play again? Enter 'y' or 'n': ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thank you!')
        break
