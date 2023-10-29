from deck import Deck
from player import Player
from dealer import Dealer
import check_input
import random

# Vansh J Gandhi
# This function compares player's and dealer's points and returns who wins.
def display_winner(pScore, dScore, points):
    if (dScore > 21 and pScore > 21) or (dScore == pScore):
        return "Tie."
    elif (pScore > 21 and dScore <= 21) or (pScore < dScore and dScore <= 21):
        points[1] += 1
        return "Dealer wins."
    elif dScore > 21 or (pScore > dScore):
        points[0] += 1
        return "Player wins."
# This is the main function this initialises the code.
def main():
    print("-Blackjack-")
    print()
    deck = Deck()
    deck.shuffle()
    points = [0, 0]  # These are points on index 0 player's points and on
                     # index 1 dealer's points

    while True:
        player = Player(deck) # Player and Dealer objects
        dealer = Dealer(deck)

        print("Player's Cards:")
        print(player.__str__())

        while True:
            print("1. Hit")
            print("2. Stay")
            choice = check_input.get_int_range("Enter choice: ", 1, 2)
            print()
            if choice == 1:
                print("Player's Cards:")
                player.hit()
                print(player.__str__())
                if player.score() > 21:
                    print('Bust!')
                    print()
                    break
            elif choice == 2:
                break

        print("Dealer's Cards:")
        dealer.play()
        print()
        print(display_winner(player.score(), dealer.score(), points))
        print(f"Player's points: {points[0]}")
        print(f"Dealer's points: {points[1]}")

        play_again = check_input.get_yes_no("Play again? (Y/N): ")
        print()

        if play_again == False:
            break


main()
