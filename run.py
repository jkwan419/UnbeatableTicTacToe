from tictactoe import TicTacToe
from player import Player

def main():
    p1 = HumanPlayer()
    p2 = AIPlayer()

    ttt = TicTacToe()

    ttt.play(p1, p2)