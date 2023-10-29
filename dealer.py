from player import Player

class Dealer(Player):
     def play(self):
        super().__str__()
        while self.score() <= 16:
            print(f"Score = {self.score()}")
            print("Dealer Hits!")
            self.hit()
            print()
            print("Dealer's Cards:")
            print(super().__str__())



