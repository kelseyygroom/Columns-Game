import copy
import random
import pygame

def find_bottom_empty(board: [list], column: int) -> int or None:
    '''
    Finds the bottommost empty row in a given column, so that any holes
    specified in the starting board can be filled.
    '''

    for i in range(len(board)-1, -1, -1):
        if board[i][column] == ' ':
            return i
    
    return None  # if the whole column is full, bottom empty = None  

   
def faller_on_board(board: [list]) -> bool:
    '''Given a gameboard, checks if a faller exists on the board and returns T/F.'''
    
    for row in board:
        for column in row:
            if '[' in column:
                return True
            if '|' in column:
                return True

    return False



class GameState():
    def __init__(self):
        self.board = [[' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', 'Y', 'Y', 'S', 'Y', ' ']]
        self.game_over = False

    def board(self):
        pass

    def faller(self):
        pass

    def game_over(self):
        pass

    def match_on_board(self)-> bool:
        for row in self.board:
            for column in row:
                if '*' in column:
                    return True

        return False


class GameMoves():
    def __init__(self):
        pass

    
    def combining_jewels(self, og_board: [list]) -> [list]:
        '''
        Given a board, checks for horizontal, vertical, and diagonal jewel
        combinations and performs combinations. Returns the updated board.
        '''

        board = copy.deepcopy(og_board)
        
        # for ensuring that the loop doesn't check for elements out of range
        row_ends = [len(board) - 1, len(board) - 2]
        col_ends = [len(board[0]) - 1, len(board[0]) - 2]
        
        unfrozen = ['|', '[']
        
        for row in range(len(board)):
            for i, col in enumerate(board[row]):
                counter = 0
                if col != ' ' and (row not in row_ends) and col[0] not in unfrozen:
                    if board[row+1][i] == col and board[row+2][i] == col:
                        while row+counter <= 12 and board[row+counter][i] == col: # only match jewels that are in a row!!
                            if len(board[row+counter][i]) == 3:
                                col = board[row+counter][i][1]
                            replace = f'*{col}*'
                            og_board[row+counter][i] = replace
                            counter += 1

                counter = 0             
                if col != ' ' and (i not in col_ends) and col[0] not in unfrozen:
                    if board[row][i+1] == col and board[row][i+2] == col: # checking for horizonatal combinations
                        while i+counter <= 5 and board[row][i+counter] == col:
                            if len(board[row][i+counter]) == 3: # make sure to combine jewels that have been included in other combinations
                                col = board[row][i+counter][1]
                            replace = f'*{col}*'
                            og_board[row][i+counter] = replace
                            counter += 1

                counter = 0               
                if col != ' ' and (i not in col_ends) and (row not in row_ends) and col[0] not in unfrozen:
                    if board[row+1][i+1] == col and board[row+2][i+2] == col: # checking for diagonal combinations
                        while row+counter <= 12 and i+counter <= 5 and board[row+counter][i+counter] == col:
                            if len(col) == 3:
                                col = col[1]
                            replace = f'*{col}*'
                            og_board[row+counter][i+counter] = replace
                            counter += 1

        return og_board



    def create_faller(self, board: [list], gamestate: 'GameState') -> [int, list]:
        '''
        Given a gameboard and GameState object, creates a faller in a random non-filled column with
        a random combination of 3 jewels. Returns a list which contains the column number (as an index)
        and the faller (as a list of three jewels).
        '''

        open_columns = []
        jewels = ['S', 'T', 'V', 'W', 'X', 'Y', 'Z']

        # checks columns and only appends open columns
        for column in range(6):
            if board[0][column] == ' ' and board[1][column] == ' ' and board[2][column] == ' ':
                open_columns.append(column)

        # random combination of three jewels
        jewel1 = f'[{random.choice(jewels)}]'
        jewel2 = f'[{random.choice(jewels)}]'
        jewel3 = f'[{random.choice(jewels)}]'

        f_jewels = [jewel1, jewel2, jewel3]


        # if all columns are full, randomly chooses any column (which would later initiate game over)
        try:
            column = random.choice(open_columns)
        except:
            column = random.randrange(5)


        f = [column, f_jewels]
        gamestate.faller = f

        
        return f


    def drop_faller(self, faller_:[int, list], board:[list], gamestate: 'GameState', moves: 'GameMoves') -> [list]:
        '''
        Given a faller, gameboard, GameState object, and GameMoves object, checks the status of the faller on the board and
        drops accordingly. Returns the updated gameboard.
        '''
        
        column = moves.faller[0]
        jewels = 'STVWXYZ'


        # drops and/or adds faller depending on status of the board
        if len(moves.faller[1]) == 0:
            faller = None
        else:
            faller = moves.faller[1]
        
        if faller == None and faller_on_board(board): # if faller is fully on board
            for r in range(12, -1, -1):
                for c in range(6):
                    if r != 12:
                        if '[' in board[r][c] and board[r+1][c] == ' ':
                            board[r+1][c] = board[r][c]
                            board[r][c] = ' '

            return board

        elif faller != None and len(faller) == 3: # if faller isn't on board at all
            if board[0][column] == ' ':
                board[0][column] = faller[0]
                
                faller.remove(faller[0])
                moves.faller = [column, faller]
                gamestate.board = board
                
                return board       
        
        elif faller != None and len(faller) == 2: # if one jewel from faller is on board
            if board[1][column] == ' ' and  '[' in board[0][column]:
                board[1][column] = board[0][column]
                board[0][column] = faller[0]

                faller.remove(faller[0])
                moves.faller = [column, faller]
                gamestate.board = board

                return board
        
        elif faller != None and len(faller) == 1: # if two jewels from faller are on board
            if board[2][column] == ' ' and  '[' in board[0][column] and '[' in board[1][column]: 
                board[2][column] = board[1][column]
                board[1][column] = board[0][column]
                board[0][column] = faller[0]


                faller.remove(faller[0])
                moves.faller = [column, faller]
                gamestate.board = board

                return board
                
        return board

                
    def next_move(self, board: [list], moves: 'GameMoves', gamestate: 'GameState', clock: 'pygame.Clock') -> [list]:
        '''
        Given an input for a move, a game board, and GameMoves and GameState
        objects, checks what the next move should be and makes calls within
        the class to perform those moves. Returns the updated board.
        '''

        jewels = 'STVWXYZ'


        for r, row in enumerate(board):
            for i, col in enumerate(row):
                if '*' in col:
                    updated_board = self.eliminate_combined(board)
                    return self.fill_holes(updated_board) # returns board where jewels have been combined and disappeared
                if '[' in col:
                    if r != 12 and (r + 3 <= 12) and (board[r+1][i] == ' ' or board[r+2][i] == ' ' or board[r+3][i] == ' '):
                        return self.drop_faller(moves.faller, board, moves, gamestate) # returns board where faller dropped
                    elif r != len(board) - 1 and '[' in board[r+2][i]:
                        return self.land_faller(board) # returns board where faller lands
                if '|' in col:
                    return self.freeze_faller(board) # returns board where faller is frozen

        # if no faller on board, create a faller
        if not(faller_on_board(board)):
            faller = self.create_faller(board, gamestate)
            moves.faller = faller
            return self.drop_faller(faller, board, moves, gamestate)

        gamestate.game_over = True
        return board

                
            
    def fill_holes(self, board: [list]) -> [list]:
        '''
        If any holes are specified in the contents of the starting board, this
        function fills all holes and returns the updated board.
        '''

        # find the bottom of each column and drop all jewels to the bottom
        for x in range(len(board)-1, -1, -1):
            for i, v in enumerate(board[x]):
                if v != ' ':
                    bottom = find_bottom_empty(board, i)
                    if bottom != None and bottom >= x:
                        board[bottom][i] = board[x][i]
                        board[x][i] = ' '
        
        return board


    def eliminate_combined(self, board: [list]) -> [list]:
        '''
        If any combinations have been found and indicated in the printed board,
        the combined jewels are removed and the updated board is returned.
        '''

        # remove all matched jewels
        for r, row in enumerate(board):
            for c, col in enumerate(row):
                if '*' in col:
                    board[r][c] = ' '

        return board            


    def rotate_faller(self, board: [list], moves: 'GameMoves') -> [list]:
        '''
        Given a board and GameMoves object, rotates a faller (if one currently
        exists on the board). Returns the updated board.
        '''
        
        faller = []

        # only works when faller is fully on board :(
        for r, row in enumerate(board):
            for c, col in enumerate(row):
                if '[' in col or ('|' in col):

                    # rearrange the faller list
                    faller.append(board[r+2][c])
                    faller.append(board[r][c])
                    faller.append(board[r+1][c])

                    # add faller to board
                    board[r][c] = faller[0]
                    board[r+1][c] = faller[1]
                    board[r+2][c] = faller[2]

                    return board

        return board


    def land_faller(self, board: [list]) -> [list]:
        '''
        Lands a faller that can no longer be moved downward. Returns updated
        board.
        '''

        # replace [ with |
        for r, row in enumerate(board):
            for c, col in enumerate(row):
                if '[' in col:
                    jewel = col[1]
                    replace = f'|{jewel}|'
                    board[r][c] = replace

        return board
                    

    def freeze_faller(self, board: [list]) -> [list]:
        '''Freezes a faller that has landed. Returns updated board.'''

        # remove '|'
        for r, row in enumerate(board):
            for c, col in enumerate(row):
                if '|' in col:
                    jewel = col[1]
                    board[r][c] = jewel

        return board


    def move_left(self, og_board: [list], moves: 'GameMoves') -> [list]:
        '''
        If a faller exists on the game board, checks if the left is open and
        moves the faller over. Returns updated game board.
        '''
        
        # only moves left if column is fully open
        board = copy.deepcopy(og_board)
        for r, row in enumerate(board):
            for c, col in enumerate(row):
                if ('[' in col or '|' in col) and c != 0:
                    if board[r][c-1] == ' ':
                        og_board[r][c-1] = col
                        og_board[r][c] = ' '
                        moves.faller[0] = c-1
                    else:
                        return board
        
        return og_board
    



    def move_right(self, og_board: [list], moves: 'GameMoves') -> [list]:
        '''
        If a faller exists on the game board, checks if the right is open and
        moves the faller over. Returns updated game board.
        '''

        # only moves right if column is fully open
        board = copy.deepcopy(og_board)
        for r, row in enumerate(board):
            for c, col in enumerate(row):
                if ('[' in col or '|' in col) and c != len(board[r]) - 1:
                    if board[r][c+1] == ' ':
                        og_board[r][c+1] = col
                        og_board[r][c] = ' '
                        moves.faller[0] = c+1
                    else:
                        return board
        
        return og_board



