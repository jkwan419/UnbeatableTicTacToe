import random

from tictactoe import TicTacToe
from player import HumanPlayer, AIPlayer

'''
Game runner
'''

def main():
    ttt = TicTacToe()

    # start = random.randint(1, 100)
    
    # if start % 2 == 0:
    p1 = HumanPlayer('O')
    p2 = AIPlayer('X')

    ttt.play(p1, p2)
    # else:
    #     p1 = HumanPlayer('X')
    #     p2 = AIPlayer('O')

    #     ttt.play(p1, p2)
    
if __name__ == "__main__":
    main()