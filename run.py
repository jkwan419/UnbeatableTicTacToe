from tictactoe import TicTacToe
from player import HumanPlayer, AIPlayer

'''
Game runner
'''

def main():
    p1 = HumanPlayer('O')
    p2 = HumanPlayer('X')

    ttt = TicTacToe()

    ttt.play(p1, p2)
    
if __name__ == "__main__":
    main()