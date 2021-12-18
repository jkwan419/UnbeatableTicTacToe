'''
Tic Tac Toe Module
'''

class TicTacToe:

    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        print()

    def print_board_nums(self):
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
        print()

    def is_empty(self):
        return ' ' in self.board

    def get_empty_cells(self):
        return [i for i in range(9) if self.board[i] == ' ']

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.check_win(square, letter):
                self.winner = letter
            return True
        return False

    def row_win(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind * 3: (row_ind + 1) * 3]
        return all([s == letter for s in row])

    def col_win(self, square, letter):
        col_ind = square % 3
        col = [self.board[col_ind + (i * 3)] for i in range(3)]
        return all([s == letter for s in col])

    def diag_win(self, square, letter):
        if square % 2 == 0:
            d1 = [0, 4, 8]
            d2 = [2, 4, 6]
            return all([self.board[s] == letter for s in d1]) or all([self.board[s] == letter for s in d2])
        return False

    def check_win(self, square, letter):
        return self.row_win(square, letter) or self.col_win(square, letter) or self.diag_win(square, letter)

    def play(self, p1, p2):
        curr_turn = 'O'
        self.print_board_nums()

        while self.is_empty:
            square = p1.get_move() if curr_turn == 'O' else p2.get_move()

            self.make_move(square, curr_turn)
            self.print_board()

            if self.winner:
                return curr_turn

            curr_turn = 'X' if curr_turn == 'O' else 'O'

        print("Tie")