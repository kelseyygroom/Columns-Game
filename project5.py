import pygame
import project5_model


class ColumnsGame():
    def __init__(self):
        self.colors = {
            'BACKGROUND': (39, 42, 44),
            'EMPTY': (255, 255, 255),
            'S': (108, 212, 255),
            'S_M': (168, 255, 255),
            'T': (37, 64, 238),
            'T_M': (97, 154, 255),
            'V': (255, 153, 22),
            'V_M': (255, 183, 60),
            'W': (198, 116, 255),
            'W_M': (248, 176, 255),
            'X': (255, 248, 46),
            'X_M': (255, 255, 166),
            'Y': (233, 13, 32),
            'Y_M': (255, 73, 72),
            'Z': (243, 68, 199),
            'Z_M': (255, 128, 159)
            }

        # initialize the game
        self.game_in_progress = True
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((700,600), pygame.RESIZABLE)


    def surface(self):
        pass
        
        
    def display_board(self, surface: 'a window', board: [list], matching_animation: bool) -> None:
        '''
        Given a surface to draw on, a board, and whether or not the matching animation needs to occur,
        displays the board in the window. Returns nothing.
        '''
        
        surface.fill(self.colors['BACKGROUND'])
        row = 0
        for r in board:
            row += 40
            column = 200
            for c in r: # displays each square/jewel depending on whether it's matched, falling, etc...
                if 'S' in c:
                    if '|' in c:
                        pygame.draw.rect(surface, self.colors['S_M'], pygame.Rect(column, row, 40, 40), 0, 2, 2)
                    elif '*' in c and matching_animation:
                        pygame.draw.rect(surface, self.colors['BACKGROUND'], pygame.Rect(column, row, 40, 40), 0, 2, 2)
                    else:
                        pygame.draw.rect(surface, self.colors['S'], pygame.Rect(column, row, 40, 40), 0, 2, 2)
                elif 'T' in c:
                    if '|' in c:
                        pygame.draw.rect(surface, self.colors['T_M'], pygame.Rect(column, row, 40, 40), 0, 2, 2)
                    elif '*' in c and matching_animation:
                        pygame.draw.rect(surface, self.colors['BACKGROUND'], pygame.Rect(column, row, 40, 40), 0, 2, 2)
                    else:
                       pygame.draw.rect(surface, self.colors['T'], pygame.Rect(column, row, 40, 40), 0, 2, 2) 
                elif 'V' in c:
                    if '|' in c:
                        pygame.draw.rect(surface, self.colors['V_M'], pygame.Rect(column, row, 40, 40), 0, 2, 2)
                    elif '*' in c and matching_animation:
                        pygame.draw.rect(surface, self.colors['BACKGROUND'], pygame.Rect(column, row, 40, 40), 0, 2, 2)
                    else:       
                        pygame.draw.rect(surface, self.colors['V'], pygame.Rect(column, row, 40, 40), 0, 2, 2)
                elif 'W' in c:
                    if '|' in c:
                        pygame.draw.rect(surface, self.colors['W_M'], pygame.Rect(column, row, 40, 40), 0, 2, 2)
                    elif '*' in c and matching_animation:
                        pygame.draw.rect(surface, self.colors['BACKGROUND'], pygame.Rect(column, row, 40, 40), 0, 2, 2)
                    else:
                        pygame.draw.rect(surface, self.colors['W'], pygame.Rect(column, row, 40, 40), 0, 2, 2)
                elif 'X' in c:
                    if '|' in c: 
                        pygame.draw.rect(surface, self.colors['X_M'], pygame.Rect(column, row, 40, 40), 0, 2, 2)
                    elif '*' in c and matching_animation:
                        pygame.draw.rect(surface, self.colors['BACKGROUND'], pygame.Rect(column, row, 40, 40), 0, 2, 2)
                    else:
                        pygame.draw.rect(surface, self.colors['X'], pygame.Rect(column, row, 40, 40), 0, 2, 2)
                elif 'Y' in c:
                    if '|' in c:
                        pygame.draw.rect(surface, self.colors['Y_M'], pygame.Rect(column, row, 40, 40), 0, 2, 2)
                    elif '*' in c and matching_animation:
                        pygame.draw.rect(surface, self.colors['BACKGROUND'], pygame.Rect(column, row, 40, 40), 0, 2, 2)
                    else:
                        pygame.draw.rect(surface, self.colors['Y'], pygame.Rect(column, row, 40, 40), 0, 2, 2)
                elif 'Z' in c:
                    if '|' in c:     
                        pygame.draw.rect(surface, self.colors['Z_M'], pygame.Rect(column, row, 40, 40), 0, 2, 2)
                    elif '*' in c and matching_animation:
                        pygame.draw.rect(surface, self.colors['BACKGROUND'], pygame.Rect(column, row, 40, 40), 0, 2, 2)
                    else:
                        pygame.draw.rect(surface, self.colors['Z'], pygame.Rect(column, row, 40, 40), 0, 2, 2)

                pygame.draw.rect(surface, self.colors['EMPTY'], pygame.Rect(column, row, 40, 40), 1)
                column += 40
        pygame.draw.rect(surface, self.colors['EMPTY'], pygame.Rect(200, 40, 40*6, 40*13), 2) # draw a border rectangle so that all lines are equal thickness
        
        
    def display_game_over(self, surface: 'a window') -> None:
        '''Given a surface to draw on, displays 'GAME OVER' in the window. Returns nothing.'''
        
        font = pygame.font.Font('freesansbold.ttf', 65)
        text = font.render('GAME OVER', True, (255, 255, 255), (0, 0, 0))
                 
        textbox = text.get_rect()
         
        textbox.center = (320, 260)
        surface.blit(text, textbox)
        pygame.display.flip() # display 'GAME OVER'


    def match_animation(self, surface: 'a window', gameboard: [list], clock: 'pyamge.Clock') -> None:
        '''
        Given a surface to draw on, the gameboard, and a clock, displays a blinking animation on matched pieces
        before they disappear. Returns nothing.
        '''

        # display the board a few times so matched jewels create a blinking effect
        self.display_board(surface, gameboard, True)
        pygame.display.flip()
        clock.tick(5)

        self.display_board(surface, gameboard, False)
        pygame.display.flip()
        clock.tick(5)
        
        self.display_board(surface, gameboard, True)
        pygame.display.flip()
        clock.tick(5)


    def handle_events(self, board: [list], gamestate: 'GameState', moves: 'GameMoves') -> None:
        '''
        Given a gameboard, GameState object, and GameMoves object, handles any events that occur and takes
        action accordingly. Returns nothing.
        '''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_in_progress = False # exit the game loop when window is closed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    board = moves.move_right(board, moves) # move faller to the right when right arrowkey is pressed
                    gamestate.board = board
                
                if event.key == pygame.K_LEFT:
                    board = moves.move_left(board, moves) # move faller to the left when left arrowkey is pressed
                    gamestate.board = board
                
                if event.key == pygame.K_SPACE:
                    board = moves.rotate_faller(board, moves) # rotate faller when spacebar is pressed
                    gamestate.board = board
            if event.type == pygame.VIDEORESIZE:
                self.resize_surface(event.size) # resize the game when user resizes window


    def resize_surface(self, size: (int, int)) -> None:
        '''
        Given the window size as a tuple of integers, resizes the game according to window size. Returns
        nothing.
        '''

        pygame.display.set_mode(size, pygame.RESIZABLE)

                
    def run(self) -> None:
        '''Implements the game mechanics in the model, and runs the game.'''

        surface = pygame.display.get_surface()

        # initialize GameState and GameMoves objects
        state = project5_model.GameState()
        moves = project5_model.GameMoves()

        gameboard = state.board # initial gameboard 

        clock = self.clock

        self.display_board(surface, gameboard, False)

        while self.game_in_progress:
        
            self.handle_events(gameboard, state, moves)
            clock.tick(2) # tick the faller down every second
            gameboard = moves.next_move(state.board, state, moves, clock)
            
                    
            state.board = moves.combining_jewels(gameboard) # check for jewel combos
            gameboard = state.board

            if state.match_on_board(): # check for matching
                self.match_animation(surface, gameboard, clock)
                

            self.display_board(surface, gameboard, False)

        
            if state.game_over: # check game over and display 'GAME OVER' when the game ends
                
                self.display_game_over(surface)
                clock.tick(1)
                
                self.game_in_progress = False
        
            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    game = ColumnsGame()
    game.run()

