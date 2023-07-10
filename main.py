import sys
from Classes.Blackjack import Blackjack
import time



class Game():
    
    def __init__(self):
        self.bj = Blackjack()
    
    
    def intro(self):
        
        answer = input('Would you like to sit down at the blackjack table? [yes/no] ')
        answer = answer.lower().strip()
        if answer == 'no' or answer == 'n':
            print('\nThis game only supports blackjack at the moment, goodbye!')
            time.sleep(3)
            quit()
        self.new_player()
        print(f'\nYou sit down at an empty table. The Dealer has a nametage that reads {self.bj.dealer.name}')
        print('\nYou have $500 in chips to start.')
    
    
    
    def new_player(self):
        name = input('\nWhats your name? ')
        name = name.title().strip()
        print(self.bj.add_player(name))
    
    
    def get_choice(self):
        for player in self.bj.table:
            if player != 'empty':
                while True:
                    res = player.check()
                    if res == 'Blackjack':
                        print(f'\nBlackjack!')
                        break
                    elif res == 'Bust':
                        print('\nBust')
                        player.clear()
                        break
                    elif res == 21:
                        print('\n21! Thats a stand.')
                        break
                    while True:
                        print(f'\nDealer {self.bj.dealer.name} is showing {self.bj.dealer.cards[0]}')
                        answer = input(f'\n{player.name} you have a {player.cards} for a {player.total} would you like to hit or stand? h for hit. s for stand. [h/s] ')
                        answer = answer.lower().strip()
                        if answer == 's' or answer == 'h':
                            break
                        else:
                            print('\nPlease enter a valid response either h or s.')
                    if answer == 'h':
                        self.bj.hit(player)
                    else:
                        print(f'\n{player.name} Stands at a {player.total}.\n')
                        break
    
    
    def scoring(self):
        while True:
            decide = self.bj.dealer.decide()
            print(f'\nDealer {self.bj.dealer.name} shows {self.bj.dealer.cards} for a {self.bj.dealer.total}.')
            if decide == 'Blackjack':
                print('Dealer blackjack!')
                break
            elif decide == 'Bust':
                print('Dealer Bust')
                self.bj.dealer.clear()
                break
            elif decide == 'Stand':
                print('Dealer stands!')
                break
            else:
                self.bj.hit(self.bj.dealer)
            time.sleep(2)
        for player in self.bj.table:
            if player != 'empty' and player.bet > 0:
                if player.check() == self.bj.dealer.check():
                    print(f'\n{player.name} pushes the dealer and gets there bet back.')
                    player.money += player.bet
                    player.clear()
                elif self.bj.dealer.check() == 'Blackjack':
                    print(f'\n{player.name} sorry Dealer wins with a Blackjack.')
                    player.clear()
                elif player.check() == 'Blackjack':
                    print(f'\n{player.name} beats Dealer with a Blackjack.')
                    player.money += player.bet * 2
                    player.clear()
                elif self.bj.dealer.total > player.total:
                    print(f"\nDealer's {self.bj.dealer.total} beats {player.name}'s {player.total}.")
                    player.clear()
                elif self.bj.dealer.total < player.total:
                    print(f"\n{player.name}'s {player.total} beats Dealer's {self.bj.dealer.total}.")
                    player.money += player.bet * 2
                    player.clear()
                time.sleep(3)
        self.bj.dealer.clear()
    
    
    def main_loop(self):
        while self.bj.table.count('empty') < 6:
            while True:
                answer = input('\nWould any new players like to join the game? [y/n] ')
                if answer == 'y':
                    self.new_player()
                elif answer == 'n':
                    break
                else:
                    print('Please enter y for yes or n for no.')
            for player in self.bj.table:
                if player != 'empty':
                    if self.bj.take_bet(player) == 'leave':
                        self.bj.remove_player(player.seat)
            if self.bj.table.count('empty') < 6:
                self.bj.deal()
                self.get_choice()
                self.scoring()
        quit()

def main():
    game = Game()
    game.intro()
    game.main_loop()
    
    
if __name__ == '__main__':
    main()