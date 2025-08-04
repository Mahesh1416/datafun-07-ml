from dataclasses import dataclass

@dataclass
class Card:
    face: str
    suit: str

    FACES = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __str__(self):
        return f'{self.face} of {self.suit}'
