import random
import numpy as np
from collections import deque

class Play2048:

    _WINING_NUM = 2048
    _DIMENSION = None

    def __init__(self, dimension):
        print(f"Start playing {dimension}X{dimension} 2048")
        self._DIMENSION = dimension
        self.valid = True # still has valid moves
        self.ws = self._DIMENSION**2 # white spaces count
        self.valid_keys = ['w', 'a', 's', 'd']
        self.win = False

        self.board = np.full([self._DIMENSION, self._DIMENSION], None)
        self.random_tile()
        self.random_tile()

    def print_board(self, msg=None):
        if msg:
            print(msg)
        print('*'*10)
        print(self.board)
        print('*'*10)

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
        return (random.randint(0, self._DIMENSION-1), random.randint(0, self._DIMENSION-1))

    def move_up(self):
        # TODO
        # print("moving up")
        # self.print_board('before rotation')
        self.board = np.rot90(self.board, 1)
        # self.print_board('after first rotation')
        self.calc_new_state()
        # self.print_board('after calc and before second rotation')
        self.board = np.rot90(self.board, 3)
        # self.print_board('after second rotation')
        self.random_tile()

        self.is_winner()

    def move_down(self):
        # TODO
        print("moving down")
        self.board = np.rot90(self.board, 3)
        self.calc_new_state()
        self.random_tile()
        self.board = np.rot90(self.board, 1)
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
        self.board = np.rot90(self.board, 2)
        self.is_winner()


    def calc_new_state(self):
        '''
        all computations are done from right to left
        '''
        # TODO

        for i in range(self._DIMENSION):
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
        lst = self.pop_n(lst)
        lst.extend([None]*(self._DIMENSION-len(lst)))
        return lst

    def calc_single(self, lst):

        if not any(lst): # all tiles equal None
            return lst

        return self.compare(self.pop_n(lst.tolist()))

    def is_winner(self):
        if self._WINING_NUM in self.board:
            self.win = True
            self.valid = False

    @staticmethod
    def random_val():
        return 2

    def random_tile(self):
        empty_tiles = np.argwhere(self.board == None)
        if len(empty_tiles) > 0: # no empty tiles left
            tile = empty_tiles[random.randint(0, len(empty_tiles)-1)].tolist()
            self.board[tile[0], tile[1]] = self.random_val()
            self.ws -= 1
