class Player():
    
    def __init__(self, name, seat, money = 500):
        self.name = name
        self.seat = seat
        self.money = 500
        self.cards = []
        self.total = 0
        self.bet = 0
    
    
    def __str__(self):
        return f'Player: {self.name}'
    
    
    def __repr__(self):
        f'Player: {self.name}'
    
    
    def clear(self):
        self.cards = []
        self.total = 0
        self.bet = 0
    
    
    def check(self):
            self.card_total()
            if self.total == 21 and len(self.cards) == 2:
                return 'Blackjack'
            elif self.total > 21:
                return 'Bust'
            else:
                return self.total
    
    
    def card_total(self):
        card_values = [card.value for card in self.cards]
        card_values.sort()
        self.total = sum(card_values)
        while 11 in card_values and self.total > 21:
            card_values.pop()
            self.total -= 10
    
    
    def print_cards(self):
        return ', '.join([str(card) for card in self.cards])



def test():
    player1 = Player('Bob', 0)
    player1.print_cards()
    
    
    


if __name__ == '__main__':
    test()