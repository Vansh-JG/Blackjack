class Card:
    Rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    Suit = ["Clubs", "Diamonds", "Hearts", "Spades"]

    def __init__(self, suit, rank):
        self._rank = rank
        self._suit = suit

    @property
    def get_rank(self):
        return self.Rank[self._rank]

    @property
    def get_suit(self):
        return self.Suit[self._suit]


    def __str__(self):
        return f"{self.get_rank} of {self.get_suit}"

    def __lt__(self, other):
        return self._rank < other._rank
