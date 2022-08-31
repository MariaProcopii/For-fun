import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]
    def __str__(self):
        return f"{self.suit} {self.rank}"


class Deck():
    def __init__(self):
        self.all_cards = []
        self.split1 = []
        self.split2 = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def split(self):
        self.split1.clear()
        self.split2.clear()
        self.split1.extend(self.all_cards[0:26])
        self.split2.extend(self.all_cards[26:])
        self.all_cards.clear()

our_deck = Deck()
our_deck.shuffle()
our_deck.split()

class Player():
    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.cards = []
        self.extracted_card = []
    def __str__(self):
        return f"Player {self.index} {self.name} has {len(self.cards)} cards"

    def add_cards(self):
        if(self.index == 1):
            self.cards.extend(our_deck.split1)
        else:
            self.cards.extend(our_deck.split2)

    def extract(self):
       self.extracted_card = self.cards.pop(0)

    def add_one(self, card):
        self.cards.append(card)

player1 = Player("Mary", 1)
player2 = Player("Alex", 2)
player1.add_cards()
player2.add_cards()

game = True
raund = 0

while game:
    raund += 1
    print(f"raund : {raund}")

    if(len(player1.cards) == 0):
        print("------------------------------------------")
        print(f"{player1.name} lose")
        print(player2)
        print("------------------------------------------")
        game = False
        break

    elif(len(player2.cards) == 0):
        print("------------------------------------------")
        print(f"{player2.name} lose")
        print(player1)
        print("------------------------------------------")
        game = False
        break

    else:
        player1.extract()
        player2.extract()

        if(player1.extracted_card.value > player2.extracted_card.value):
            print(f"{player1.extracted_card} ({player1.extracted_card.value}) "
                  f"is bigger than {player2.extracted_card} "
                  f"({player2.extracted_card.value})")
            player1.add_one(player2.extracted_card)

        elif(player1.extracted_card.value == player2.extracted_card.value):
            print("Tie. Cards removed from the players deck")

        else:
            print(f"{player2.extracted_card} ({player2.extracted_card.value}) "
                  f"is bigger than {player1.extracted_card} "
                  f"({player1.extracted_card.value})")
            player2.add_one(player1.extracted_card)


