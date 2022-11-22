# Classes and initalizatoin below

from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 11,
    'Queen': 12,
    'King': 13,
    'Ace': 14
}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank.capitalize()]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        shuffle(self.all_cards)

    def deal(self):
        return self.all_cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    
    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'{self.name} has {len(self.all_cards)} cards.'

# Game logic starts below

player_one = Player('one')
player_two = Player('two')

new_deck = Deck()
new_deck.shuffle()

for card in range(26):
    player_one.add_cards(new_deck.deal())
    player_two.add_cards(new_deck.deal())

is_game_on = True

round = 0

while is_game_on:
    round += 1
    print(f'Round {round}')

    if len(player_one.all_cards) == 0:
        print('Player Two wins as Player One has no cards left!')
        is_game_on = False
        break
    if len(player_two.all_cards) == 0:
        print('Player One wins as Player Two has no cards left!')
        is_game_on = False
        break

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True
    
    while at_war:

        if player_one_cards[-1] > player_two_cards[-1]:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_one_cards[-1] < player_two_cards[-1]:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False

        else:
            print('WAR!')
            
            if len(player_one.add_cards) < 3:
                print('Player 1 was unable to declare war')
                print("PLAYER 2 WINS!")
                is_game_on = False
                break

            elif len(player_two.add_cards) < 3:
                print('Player 2 was unable to declare war')
                print("PLAYER 1 WINS!")
                is_game_on = False
                break


