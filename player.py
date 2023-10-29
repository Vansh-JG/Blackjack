from card import Card
from deck import Deck

class Player:
    def __init__(self, deck):
        self._deck = deck
        self._hand = []
        self._hand.append(self._deck.draw_card())
        self._hand.append(self._deck.draw_card())
        self._hand.sort()

    def hit(self):
        self._hand.append(self._deck.draw_card())
        self._hand.sort()

    def score(self):
        score_player = 0
        for card in self._hand:
            if card._rank in (9, 10, 11):
                score_player += 10
            elif card._rank == 12:
                if score_player < 11:
                    score_player += 11
                else:
                    score_player += 1
            elif card._rank in (0, 1, 2, 3, 4, 5, 6, 7, 8):
                score_player += int(card._rank + 2)
        return score_player


    def __str__(self):
        for i in self._hand:
            print(i)
        return f"Score = {self.score()}"






