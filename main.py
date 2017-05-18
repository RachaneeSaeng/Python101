from __future__ import print_function 
from IPython.display import clear_output
import random

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = raw_input('Player 1: Do you want to be X or O?').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')   
  
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'  
    
def play_game(board, player_marker):    
    position = player_choice(board)
    place_marker(board, player_marker, position)
    display_board(board)
    
    if win_check(board, player_marker, position):        
        print('Congratulations! You have won the game!')
        return True
    else:
        if full_board_check(board):            
            print('The game is a draw!')
            return True
    return False

def display_board(board):
    clear_output()
    print('               ')    
    print(' ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print('-----------')
    print(' ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])    
    print('-----------')
    print(' ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])

def player_choice(board):
    # Using strings because of raw_input
    position_number = ' '    
    while position_number not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, position_to_matrix(int(position_number))):        
        position_number = raw_input('Choose your next position: (1-9) ')
    return position_to_matrix(int(position_number))

def position_to_matrix(position_number):
    return {'row': int((position_number-9) / -3), 'col': (position_number-1) % 3}

def space_check(board, position):
    return board[position['row']][position['col']] == ' '

def place_marker(board, marker, position):   
    board[position['row']][position['col']] = marker

def full_board_check(board):
    for position in range(1,10):
        if space_check(board, position_to_matrix(position)):
            return False
    return True

def win_check(board, mark, position):
    # Check row
    if(len(set(board[position['row']])) == 1):
        return True
    # Check column
    if(len(set([x[position['col']] for x in board])) == 1):
        return True
    # Check diagonal
    return (mark == board[1][1] == board[0][0] == board[2][2]) or (mark == board[1][1] == board[0][2] == board[2][0])

def replay():
    return raw_input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    theBoard = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    #Displa startup board
    display_board(theBoard)
    
    while True:
        if turn == 'Player 1':
            if play_game(theBoard, player1_marker):
                break
            else:
                turn = 'Player 2'            
        else:
            if play_game(theBoard, player2_marker):
                break
            else:
                turn = 'Player 1'                
    if not replay():
        break

