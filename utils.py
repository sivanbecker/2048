import random
import numpy as np
from collections import deque

class Play2048:

    def __init__(self):
        print("Start playing 2048")
        self.valid = True # still has valid moves
        self.ws = 16 # white spaces count
        self.valid_keys = ['w', 'a', 's', 'd']
        self.win = False

        self.board = np.full([4, 4], None)

        init_row_1 = random.randint(0, 3)
        init_col_1 = random.randint(0, 3)
        init_row_2 = random.randint(0, 3)
        init_col_2 = random.randint(0, 3)

        self.board[self.rand_cell()] = 2
        self.board[self.rand_cell()] = 2
        # self.board[init_row_1][init_col_1] = 2
        # self.board[init_row_2][init_col_2] = 2

        c00 = c01 = c02 = c03 = None # row0
        c10 = c11 = c12 = c13 = None # row1
        c20 = c21 = c22 = c23 = None # row2
        c30 = c31 = c32 = c33 = None # row3

        row0 = deque([c00, c01, c02, c03])
        row1 = deque([c10, c11, c12, c13])
        row2 = deque([c20, c21, c22, c23])
        row3 = deque([c30, c31, c32, c33])

        self.rows = [row0, row1, row2, row3]

        col0 = [row0[0], row1[0], row2[0], row3[0]]
        col1 = [row0[1], row1[1], row2[1], row3[1]]
        col2 = [row0[2], row1[2], row2[2], row3[2]]
        col3 = [row0[3], row1[3], row2[3], row3[3]]

        self.cols = [col0, col1, col2, col3]



        # TODO - what if initiated the same cell
        self.rows[init_row_1][init_col_1] = 2
        self.rows[init_row_2][init_col_2] = 2

        self.ws -= 2

    def print_board(self):
        print(self.board)
        # print(self.rows[0])
        # print(self.rows[1])
        # print(self.rows[2])
        # print(self.rows[3])

    def playing(self):
        while self.valid:
            k = input("choose w/s/a/d: ")
            if k not in self.valid_keys:
                print(f"Please choose from {self.valid_keys}")
                continue

            if k == 'w':
                self.move_up()
            elif k == 's':
                self.move_down()
            elif k == 'a':
                self.move_left()
            else:
                self.move_right()

        self.print_board()
        if self.win:
            print("You win")
        else:
            print("You lose")

    @staticmethod
    def rand_cell():
        return (random.randint(0, 3), random.randint(0, 3))

    def move_up(self):
        # TODO
        print("moving up")
        self.board = np.rot90(self.board, 1)
        self.calc_new_state()
        self.random_tile()
        self.board = np.rot90(self.board, -1)
        self.is_winner()

    def move_down(self):
        # TODO
        print("moving down")
        self.board = np.rot90(self.board, 3)
        self.calc_new_state()
        self.random_tile()
        self.board = np.rot90(self.board, -3)
        self.is_winner()

    def move_left(self):
        # TODO
        print("moving left")
        self.calc_new_state()
        self.random_tile()
        self.is_winner()

    def move_right(self):
        # TODO
        print("moving right")
        self.board = np.rot90(self.board, 2)
        self.calc_new_state()
        self.random_tile()
        self.board = np.rot90(self.board, -2)
        self.is_winner()


    def calc_new_state(self):
        '''
        all computations are done from right to left
        '''
        # TODO

        for i in range(4):
            self.board[i] = self.calc_single(self.board[i])


    def pop_n(self, lst):
        ''' remove any None values'''
        while None in lst:
            lst.remove(None)
        return lst

    def compare(self, lst):
        ''' '''

        if len(lst) > 1:

            for i in range(len(lst)-1):
                if lst[i] == lst[i+1]:
                    lst[i] = lst[i]*2
                    lst[i+1] = None

        lst.extend([None]*(4-len(lst)))
        return lst

    def calc_single(self, lst):
        ''' lst [x,y,z,w] actually a deque object
        each of x,y,z,w can be None or int
        '''
        if not any(lst): # all tiles equal None
            return lst

        return self.compare(self.pop_n(lst.tolist()))

    def is_winner(self):
        if 2048 in self.board:
            self.win = True
            self.valid = False

    def random_tile(self):
        import pudb;pu.db
        self.ws = 0
        if self.ws == 0:
            self.valid = False
        else:
            pass
