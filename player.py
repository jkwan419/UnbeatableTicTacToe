import math
import random

'''
Player Module
'''

class Player:
    
    def __init__(self, letter):
        self.letter = letter

    def get_move(self):
        pass

class HumanPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self):
        move = input("Pick a square: ")
        return int(move)

class AIPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if game.is_empty():
            return random.randint(0, 9)
        else:
            return minimax(game, self.letter)

    def minimax(self, state, player):
        other_player = 'O' if player == 'X' else 'X'

        best_move = { "position" : None, "score" : -math.inf } if self.letter == player else { "position" : None, "score" : math.inf }

        for move in state.get_empty_cells():
            pass
            
        return random.randint(0, 9)