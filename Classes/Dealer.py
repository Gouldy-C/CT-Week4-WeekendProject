from Classes.Player import Player
import random as ran

class Dealer(Player):
    NAMES = ['Sean','Dylan','James','Mary','Jennifer','John','Michael','Linda','Jessica','Karen','Anthony','Christopher','Thomas','Betty','Margaret','Donald','Matthew','Sarah']
    
    def __init__(self):
        self.name = ran.choice(self.NAMES)
        self.cards = []
        self.total = 0
    
    
    def decide(self):
        self.card_total()
        if self.total == 21 and len(self.cards) == 2:
            return 'Blackjack'
        elif 17 <= self.total <= 21:
            return 'Stand'
        elif self.total > 21:
            return 'Bust'
        else:
            return 'Hit'
    
    
    def clear(self):
        self.cards = []
        self.total = 0



def test():
    dealer = Dealer()
    print(dealer.name)
    
    
    


if __name__ == '__main__':
    test()