#!/bin/bash


#To shuffle for random cards.
import random


#Global Vars: The Suit and Ranks never change.

suits = ('♠', '♦', '♥', '♣')
ranks = ('A', '2','3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
values = {'A': 11, '2': 2,'3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
playing = True



class Card:
    """Suits and ranks are the only attributes to define the cards"""

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit




class Deck:
    """Call the card class, shuffle, deal and track use of 52 unique cards"""

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        one_card = self.deck.pop()
        return one_card



class Hand:
    """Calls the Card Class and calculates the value of the cards.
    Accounts for Ace = 1 or 11"""

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_cards(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'A':
            self.aces += 1

    def value_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1



#Game play element: Hit/Stand Question to player & add card if hit or dealer > 17
#could be a class?

def hit(deck, hand):
    """Adds one card to hand and calculates the new value"""

    hand.add_cards(deck.deal())
    hand.value_ace()

def hit_or_stand(deck, hand):
    """Asks player if they want to hit or stand on their turn"""
    #Maybe should not be using the global value here?
    global playing

    while True:
        print()
        h_or_s = input('Would you like to Hit or Stand? ').lower()

        #looks at first letter [0] of what player types.
        if h_or_s[0] == 'h':
            hit(deck, hand)

        elif h_or_s[0] == 's':
            print('Player stands. It\'s now, Veronica\'s turn.')
            playing = False

        else:
            #if they type anything else we can just move on
            print('Hmm, I don\'t know that one. Let\'s stick with the rules.')
            continue

        break




class Chips:
    """Starting chips, bets and minimum bets, winnings and losses"""

    def __init__(self):
        self.total = 10
        self.bet = 0

    def win_bet(self):
        self.total = self.total + self.bet

    def lose_bet(self):
        self.total = self.total - self.bet




#Game play element: Adding Chips and updating with wins and losses and BlackJack.

def place_bet(chips):
    """Asks for bet and checks that bet does not exceed available ships and is a number"""

    while True:
        try:
            chips.bet = int(input('Please place your bet: '))
        except ValueError:
            print('Sorry, at Veronica\'s BlackJack we only take money. Please enter a number. ')
        else:
            if chips.bet > chips.total:
                print('Opps {} is all that is in your piggy bank.'.format(chips.total))
            elif chips.bet <= 0:
                    print('You have to bet something!')
            else:
                break

def player_blackjack(player, dealer, chips):
    print()
    print('BlackJack!')
    chips.win_bet()

def player_busts(player, dealer, chips):
    print()
    print('You went over 21, you bust!')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print()
    print('Great Job. You win!')
    chips.win_bet()

def push(player, dealer):
    print()
    print('You and Veronica tie! It\'s a push. Keep your bet for another hand.')

def dealer_busts(player, dealer, chips):
    print()
    print('Veronica busts!')
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print()
    print('Veronica wins!')
    chips.lose_bet()

def dealer_blackjack(player, dealer):
    print()
    print('BlackJack!')



#Display Cards; change these to ASCII- not time forthat

def show_players_hand(player,dealer):
    print('\nVeronica\'s Hand')
    print('<Hidden>')
    print('', dealer.cards[1])
    print('\nYour Hand: ', *player.cards, sep= '\n')
    print('Your hand totals ', player.value)

def show_dealers_hand(player,dealer):
    print('\nVeronica\'s Hand:', *dealer.cards, sep="\n")
    print('Veronica\'s hand totals ',dealer.value)



#Game Rules and Play

print('Welcome to Veronica\'s BlackJack game.')
print()
print('The rules: Get the total value of your cards as close to 21 without going over.')
print()
print('Good Luck!')

pchips = Chips()

while True:

    #Create and shuffle deck.
    deck = Deck()
    deck.shuffle()

    #Create Veronica the dealer's hand and deal two cards
    veronica = Hand()
    veronica.add_cards(deck.deal())
    veronica.add_cards(deck.deal())

    #create Player's hand, deal two cards, set chips and ask for chips
    player1 = Hand()
    player1.add_cards(deck.deal())
    player1.add_cards(deck.deal())
    print()
    print('You have a total of ' + str(pchips.total) + ' chips.')
    place_bet(pchips)


    #Deal cards and start player's round
    show_players_hand(player1, veronica)

    while playing:

        hit_or_stand(deck, player1)

        show_players_hand(player1, veronica)

        if player1.value > 21:
            player_busts(player1, veronica, pchips)
            break

    if player1.value <=21:
        while veronica.value <= 17:
              hit(deck, veronica)

        show_dealers_hand(player1, veronica)

        #Determine who wins.
        if veronica.value > 21:
            dealer_busts(player1, veronica, pchips)

        elif player1.value == 21 and player1.value > veronica.value:
            player_blackjack(player1, veronica, pchips)
            player_wins(player1, veronica, pchips)

        elif player1.value > veronica.value:
            player_wins(player1, veronica, pchips)

        elif veronica.value == 21 and veronica.value > player1.value:
            dealer_blackjack(player1, veronica)
            dealer_wins(player1, veronica, pchips)

        elif veronica.value > player1.value:
            dealer_wins(player1, veronica, pchips)

        else:
            push(player1, veronica)

    print('You have a total of ' + str(pchips.total) + ' chips.')
    print()

    if pchips.total > 0:
        print()

        play_again = input('Deal again? Yes/No ').lower()

        #looks at first letter [0] of what player types.
        if play_again[0] == 'y':
            playing = True
            continue

        elif play_again[0] == 'n':
            print('Thanks for playing! Come back soon.')
            playing = False
            break

        else:
            #if they type anything else we can just move on
            print('Hmm, I don\'t know that one, but you still have chips!')

    else:
        print('Come back when you have some money.')
        break
