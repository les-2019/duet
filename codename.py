#!/usr/bin/python3
from random import choice, sample, randint, shuffle
from vocab import getWords
from keycodes import getKeyCodes

global turn
global numTurns
squares = list()
TURNS = (1,2)
# -------------------------------------------------
vocabURL = "https://www.randomlists.com/nouns?qty=25&dup=false"

# -------------------------------------------------
class Square:
    def setWord(self, word):
        self.word = word

    def __init__(self, word, color1, color2, selected):
        self.word = word
        self.color1 = color1
        self.color2 = color2
        self.selected = selected

    def __repr__(self):
        return ("({},{},{},{})".format(self.word, self.color1.name.split('.')[-1],self.color2.name.split('.')[-1], self.selected))

    def __str__(self):
        return self.__repr__()
# --------------------------------------------------
def tst_square():
    print(Square("word", Color.BLACK, False))
# --------------------------------------------------
def board_show(squares):
    print('*'*20)
    for i in range(5):
        print(i+1, ')', end='')
        print(squares[i * 5 + 0:i * 5 + 5])
        print([square.word for square in squares[i * 5 + 0:i * 5 + 5]], end='')
        print()
        print('*'*20)
# --------------------------------------------------
def board_init():
    ''' Determine team color to go first
    Set up squares of the right colors in some random order
    '''
    numTurns = 1
    turn = sample(TURNS, 1)[0]
    print("turn={}".format(turn))
    words = getWords()
    keycodes = getKeyCodes()
    keyColors = list(keycodes)
    for word in words:
        color1, color2 = keyColors.pop()
        square = Square(word, color1, color2, False)
        squares.append(square)
    shuffle(squares)
    return squares
# --------------------------------------------------
def main():
    squares = board_init()
    board_show(squares)
    return
# -------------------------------------------------
if __name__ == "__main__":
    main()
