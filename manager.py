from tabnanny import check
from player import Player
import random
import sys
#This class control the game logic
class Manager:

    def __init__(self):
        self.is_playing = True
        self.card_num= 0
        self.next_card = 0
        self.user_guess = ""
        self.card_set = []
        self.player = Player()

#starts the game
    def game_start(self):
        if (self.is_playing):
            self.card_set = [1,2,3,4,5,6,7,8,9,10,11,12,13]
            random.shuffle(self.card_set)
            self.card_num = self.card_set.pop()
            self.ask_user()
        else:
            return

#invoke a player behavior
    def ask_user(self):
            self.next_card = self.card_set.pop()
            self.player.take_guess(self.card_num)
            self.check_result()


#compare user guess with real card and ask if to play again
    def check_result(self):
        print("Next card was: %d" % self.next_card)
        if self.card_num < self.next_card and self.player.user_guess == "h":
            self.player.points += 100
            print("Your score is: %d" % self.player.points)
        elif self.card_num > self.next_card and self.player.user_guess == "l":
            self.player.points += 100
            print("Your score is: %d" % self.player.points)
        else:
            self.player.points -= 75
            print("Your score is: %d" % self.player.points)

        if self.player.points <= 0:
            print("You lost!")
            self.is_playing = False

        if len(self.card_set) == 0:
            print("You won!")

        while (self.is_playing and len(self.card_set) > 0):
            play_again = input("Play again? [y/n]")
            print("\n")
            if play_again == "y":
                self.card_num = self.next_card
                self.ask_user()
            else:
                print("Thank you!")
                self.is_playing = False
                return


