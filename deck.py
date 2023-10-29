from card import Card
import random
class Deck:
    def __init__(self):
        # self._cards: Deck of cards.
        self._cards = []
        for suit in range(len(Card.Suit)):
            for rank in range(len(Card.Rank)):
                self._cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self._cards)

    def draw_card(self):
        return self._cards.pop(0)

    def __len__(self):
        return len(self._cards)
