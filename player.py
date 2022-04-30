import random
    #This class holds player functionality by storing score and taking guess
class Player:

    def __init__(self):
        self.points = 300



        


        
    def take_guess(self, card_num):
        print("The card is %d" % card_num)
        self.user_guess = input("Higher or lower: [h/l]")
