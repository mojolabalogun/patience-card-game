import random

class Card:
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        rank = str(self.rank)
        if self.rank == 1:
            rank = "Ace"
        if self.rank == 11:
            rank = "Jack"
        if self.rank == 12:
            rank = "Queen"
        if self.rank == 13:
            rank = "King"
        return rank + " of " + self.suits[self.suit] 

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.suit == other.suit and self.rank == other.rank
        else:
            return False

class Cards:

    def __init__(self):
        self.cards = list()

    def peek(self):
        if len(self) > 0:
            return self.cards[-1]
        return None

    def __len__(self):
        return len(self.cards)

class Deck(Cards):
    def __init__(self):
        Cards.__init__(self)

        for i in range(0, 4):
            for r in range(1, 14):
                c = Card(i, r)
                self.cards.append(c)

        self.shuffle()
        self.current = 0

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            j = random.randint(0, i)
            self.cards[i],self.cards[j] = self.cards[j],self.cards[i]

    def top(self):
        return self.cards[self.pointer]

    def take(self):
        if self.current < 52:
            answer = self.cards[self.current]
        else:
            answer = None
        self.current += 1
        return answer

class InfiniteDeck():

    def __init__(self, suit, rank):
        self.card = Card(suit, rank)
        self.in_deck = bool(random.randint(0, 1))

    def generate_card(self):
        suit = random.randint(0, 3)
        rank = random.randint(1, 13)
        return Card(suit, rank)
    
    def next_card(self):
        card = self.generate_card()
        if self.in_deck:
            return card
        
        while self.card == card:
            card = self.generate_card()
        return card
        