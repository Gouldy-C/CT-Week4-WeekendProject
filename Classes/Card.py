class Card():
    VALUES_DICT = {
        1 : ['Ace',11],
        2 : ['2', 2],
        3 : ['3',3],
        4 : ['4',4],
        5 : ['5',5],
        6 : ['6',6],
        7 : ['7',7],
        8 : ['8',8],
        9 : ['9',9],
        10 : ['10',10],
        11 : ['Jack',10],
        12 : ['Queen',10],
        13 : ['King',10],
    }
    SUITS = ['Hearts','Diamonds','Clubs','Spades']
    
    
    def __init__(self, num, suit):
        if num in self.VALUES_DICT:
            self.key = num
        else:
            raise ValueError('Error in Card: Invalid Card value')
        
        if suit.title() in self.SUITS:
            self.suit = suit.title()
        else:
            raise ValueError('Error in Card: Invalid Card suit')
            
        self.face = self.VALUES_DICT[self.key][0]
        self.value = self.VALUES_DICT[self.key][1]
    
    
    def __str__(self):
        return f'{self.face} of {self.suit}'
    
    
    def __repr__(self):
        return f'{self.face} of {self.suit}'





def test():
    card_player1 = Card(1,'hearts')
    print(card_player1)
    print(card_player1.value)

    card_player2 = Card(13,'clubs')
    print(card_player2)
    print(card_player2.value)




if __name__ == '__main__':
    test()