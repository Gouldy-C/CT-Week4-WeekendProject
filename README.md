# Project Description:

For this weekend project, you will create a simplified version of the Blackjack game using Python, focusing on object-oriented programming concepts. This project aims to test your understanding of OOP while implementing a fun and interactive game.

## Rules:

The game will involve two players: the Dealer and the Player. At the start of the game, there will be a deck of 52 cards, divided into four suits: Clubs, Diamonds, Hearts, and Spades. Each suit will contain cards numbered 1 through 13 (Ace to King).

## Notes:

- There will be no wildcards used in this game.The game begins with the Dealer shuffling the deck of cards to randomize them. After shuffling, the Dealer deals two cards to the Player and two cards to itself. The Player can see both of their own cards, but can only see one of the Dealer’s cards.

- The objective of the game is for the Player to evaluate the value of their cards. If the Player is unsatisfied with their hand, they have the option to ‘Hit,’ which means requesting an additional card from the Dealer. The Player can hit as many times as they want, as long as they don’t go over a total of 21, resulting in a ‘Bust.’

- If the Player is dealt cards totaling 21 on the first deal, it is considered a ‘Blackjack’ and the Player wins. It’s important to note that Blackjack can only be attained on the first deal.

- The Player cannot see the Dealer’s complete hand until they choose to ‘Stand.’ Standing means the Player decides not to receive any more cards from the Dealer. Once the Player stands, the Player’s and the Dealer’s hands are compared. The hand with the higher total wins. Remember that the Dealer can also bust by going over 21.

## Additional Challenges for extra credit (Complete at least 2 to qualify for extra credit):

- Implement a betting system where the Player starts with a certain amount of virtual money and can place bets on each round of the game. The Player’s virtual money should increase or decrease based on whether they win or lose the round.

- Add the ability for the Player to split their hand if they are initially dealt two cards of the same rank (e.g., two Kings). This would create two separate hands to play simultaneously, doubling the betting and adding complexity to the game.

- Introduce a deck reshuffling mechanism after a certain number of rounds or when the deck reaches a certain threshold. This simulates a more realistic casino environment.

- Implement a simple graphical user interface (GUI) using a library like Tkinter or Pygame to enhance the visual appeal and user experience of the game.
