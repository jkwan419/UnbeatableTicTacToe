import math
import random

'''
Player Module
'''

class Player:
    
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class HumanPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_move = False
        square = None

        while not valid_move:
            move = input("Pick a square: ")
            try:
                square = int(move)
                if not square in game.get_empty_cells():
                    raise ValueError

                valid_move = True

            except:
                print("Invalid square. Try again...")

        return square

class AIPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.get_empty_cells()) == 9:
            return random.randint(0, 8)
        else:
            return self.minimax(game, self.letter)["position"]

    def utility(self, state, other_player):
        if self.letter == other_player:
            return len(state.get_empty_cells()) + 1
        else:
            return -1 * (len(state.get_empty_cells()) + 1)

    def minimax(self, state, player):
        other_player = 'O' if player == 'X' else 'X'

        if state.winner == other_player:
            sc = self.utility(state, other_player)
            return { "position" : None, "score" : sc }

        if len(state.get_empty_cells()) == 0:
            return { "position" : None, "score" : 0 }

        best_move = { "position" : None, "score" : -math.inf } if self.letter == player else { "position" : None, "score" : math.inf }

        for move in state.get_empty_cells():
            state.make_move(move, player)
            sim_score = self.minimax(state, other_player)

            state.board[move] = ' '
            state.winner = None
            sim_score["position"] = move

            if self.letter == player and sim_score["score"] > best_move["score"]:
                best_move = sim_score
            elif not self.letter == player and sim_score["score"] < best_move["score"]:
                best_move = sim_score

        return best_move