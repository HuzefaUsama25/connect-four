import numpy as np

class connect4:
    def __init__(self):
        self.board = [
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                ]
        self.colors = ["🔵","🔴"]


    def show_board(self):
        board = str(self.board)
        print(" 1   2   3   4   5   6   7")
        print()
        print(board.strip().replace("],","\n").replace("[","").replace("]","").replace("' '","⚪").strip().replace(",","").replace("'","").replace("\n ","\n\n").replace(" ",'  '))


    def check_row(self):
        board = self.board
        for row in board:
            for color in range(2):
                if f"{self.colors[int(f'{color}')]}"*4 in ''.join(row):
                    return self.colors[int(f"{color}")]


    def check_col(self):
        board = self.board
        for column_num in range(6):
            col_string = ""
            for row in board:
                col_string += row[column_num]
            for color in range(2):
                if f"{self.colors[int(f'{color}')]}"*4 in col_string:
                    return self.colors[int(f"{color}")]

    def get_diagonals(self):
        matrix = np.array(self.board)
        diags = [matrix[::-1,:].diagonal(i) for i in range(-3,4)]
        diags.extend(matrix.diagonal(i) for i in range(3,-4,-1))
        return [n.tolist() for n in diags]


    def check_dia(self):
        board = self.board
        diagonals = self.get_diagonals()
        for color in range(2):
            for diagonal in diagonals:
                print("".join(diagonal))
                if f"{self.colors[int(f'{color}')]}"*4  in "".join(diagonal):
                    return self.colors[int(f"{color}")]



    def check_win(self):
        if self.check_row() != None: return self.check_row()
        if self.check_col() != None: return self.check_col()
        if self.check_dia() != None: return self.check_dia()


    def add_ball(self, column, color):
        board = self.board
       
        #fixthis-start
        o = [i for i in range(len(board))]
        o.reverse()
        #fixthis-end

        for row in o:
            if board[row][column] == ' ':
                board[row][column] = self.colors[color]
                break

        self.board = board
