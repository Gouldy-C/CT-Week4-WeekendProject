from Classes.Card import Card
import random as ran


class DeckOfCards():
    def __init__(self, number_of=1):
        self.deck = []
        if number_of >= 8:
            self.num_decks = 8
        else:
            self.num_decks = number_of

        for _ in range(self.num_decks):
            for s in Card.SUITS:
                for n in Card.VALUES_DICT.keys():
                    card = Card(n, s)
                    self.deck.append(card)
        self.shuffle()
        self.original_size = len(self.deck)

    def __str__(self):
        return "\n".join([str(card) for card in self.deck])

    def __repr__(self):
        "\n".join([str(card) for card in self.deck])

    def shuffle(self):
        ran.shuffle(self.deck)
        ran.shuffle(self.deck)
        ran.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop()

    def reset_deck(self):
        self.__init__(self.num_decks)


def test():
    deck = DeckOfCards()
    print(len(deck.deck))
    print(deck.draw_card())
    print(deck.draw_card())
    print(deck.draw_card())
    print(deck.draw_card())
    print(deck.draw_card())
    print(deck.draw_card())
    print(deck.draw_card())
    print(deck.draw_card())
    print(deck.draw_card())
    print(len(deck.deck))
    deck.reset_deck()
    print(len(deck.deck))


if __name__ == '__main__':
    test()
