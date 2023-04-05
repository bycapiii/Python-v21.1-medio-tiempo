import random
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for value in range(2, 11):
                self.cards.append(Card(suit, str(value)))
            for value in ["Jack", "Queen", "King", "Ace"]:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)
        if card.value == "Ace":
            if self.value + 11 > 21:
                self.value += 1
            else:
                self.value += 11
        elif card.value in ["Jack", "Queen", "King"]:
            self.value += 10
        else:
            self.value += int(card.value)

    def __str__(self):
        return ", ".join([str(card) for card in self.cards])

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def deal_starting_hands(self):
        for i in range(2):
            self.player_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())

    def player_turn(self):
        while self.player_hand.value <= 21:
            print(f"Your hand: {self.player_hand}")
            action = input("Do you want to hit or stand? ")
            if action == "hit":
                self.player_hand.add_card(self.deck.deal_card())
            else:
                break

    def dealer_turn(self):
        while self.dealer_hand.value < 17:
            self.dealer_hand.add_card(self.deck.deal_card())

    def determine_winner(self):
        if self.player_hand.value > 21:
            print("You bust! Dealer wins")

