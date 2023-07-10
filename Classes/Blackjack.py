from Classes.Player import Player
from Classes.Dealer import Dealer
from Classes.Deck import DeckOfCards

class Blackjack():
    
    def __init__(self, num_decks = 2, table_size = 6):
        self.deck = DeckOfCards(num_decks)
        self.table = ['empty' for _ in range(table_size)]
        self.dealer = Dealer()
    
    def check_deck(self):
        if len(self.deck.deck) < ((7 - self.table.count('empty')) * 4):
            self.deck.reset_deck()
    
    
    def deal(self):
        self.check_deck()
        for _ in range(2):
            for person in self.table:
                if person != 'empty' and person.bet > 0:
                    person.cards.append(self.deck.draw_card())
            self.dealer.cards.append(self.deck.draw_card())
    
    
    def display_cards(self):
        for person in self.table:
            if person != 'empty' and person.bet > 0:
                print(f'{person.name} : {person.cards[0]}, {person.cards[1]}')
        print(f'Dealer: {self.dealer.name} : {self.dealer.cards[0]}')
    
    
    def take_bet(self, player):
        while True:
            bet = input(f'{player.name} you have {player.money}. How much would you like to bet? You can also type leave to leave the table. [Whole Integer] or [leave] ')
            if bet.lower() == 'leave':
                return bet.lower()
            try:
                bet = int(bet)
            except:
                print('Invalid bet, only whole integers or [leave] are allowed')
            if 0 <= bet <= player.money:
                player.bet = bet
                player.money -= bet
                break
            else:
                print("Invalid bet, bet can't be negative number or a number greater then the players total money")
    
    
    def split_hand(self, player):
        pass
    
    
    def hit(self, player):
        player.cards.append(self.deck.draw_card())
    
    
    def add_player(self, player_name):
        if 'empty' in self.table:
            seat = self.table.index('empty')
            name = player_name.title()
            player = Player(name, seat)
            self.table[seat] = player
            return f'Added'
        return 'Full'
    
    
    def remove_player(self, player_seat):
        self.table[player_seat] = 'empty'
    
    
    def clear_table(self):
        for person in self.table:
            if person != 'empty':
                person.clear()
        self.dealer.clear()
    
    
    
def test():
    bj = Blackjack()
    bj.add_player('christian')
    bj.add_player('christian')
    bj.add_player('max')
    bj.take_bet(bj.table[0])
    bj.take_bet(bj.table[1])
    bj.deal()
    bj.display_cards()
    bj.clear_table()
    
    
    
    
    




if __name__ == '__main__':
    test()