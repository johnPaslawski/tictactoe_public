# START of the programm
# importing modules:
# defining functions:
import sys
import os


def init_board():
    row1 = ['.','.','.']
    row2 = ['.','.','.']
    row3 = ['.','.','.']
    board = [row1, row2, row3]
    return board

# function get_move() asks for user input and returns the coordinates of a valid move on board.
def get_move():
    list_of_possible_coordinates_str = ['a', 'A', 'b', 'B', 'c', 'C']
    list_of_possible_coordinates_int = ['1', '2', '3']
    coordinates_input_is_valid = False
    
    # Function is repeating input request until proper input is given.
    # Temporary list is being made here, for keeping user coordinates or quit input for processing.
    while coordinates_input_is_valid == False:
        coordinates_given_by_user = str(input("Provide VALID coordinates (LETTER + NUMBER, e.g.: A1, C2) \n(or type 'Quit' to exit program anytime):\n"))
        coordinates_list = []

        os.system('cls' if os.name == 'nt' else 'clear')
        print_board(player_mark, board)
        print('_ _ _  ARE YOU SURE ?. . . \n')

        # Function is checking if input is 'quit', if so, it returnes 
        # 'quit' string as whole get_move() function result.
        if (coordinates_given_by_user.lower() == 'quit'):
                coordinates_given_by_user = coordinates_given_by_user.lower()
                return coordinates_given_by_user

        # user input is being processed and conditions are checked
        for coordinates_given_by_user_iteration_counter in coordinates_given_by_user:
            coordinates_list.append(coordinates_given_by_user_iteration_counter)      
        if (len(coordinates_list) == 2) or (len(coordinates_list) == 4):
            if (coordinates_list[0] in list_of_possible_coordinates_str) and (coordinates_list[1] in list_of_possible_coordinates_int):
                coordinates_input_is_valid = True

                # value of variable 'col' is already an integer;
                # ;whereas variable 'row' value assigning requires following processing from string to integer :
                col = int(coordinates_list[1])
                row = int()
                if coordinates_list[0] == 'a' or coordinates_list[0] == 'A':
                    row = 0
                elif coordinates_list[0] == 'b' or coordinates_list[0] == 'B':
                    row = 1
                elif coordinates_list[0] == 'c' or coordinates_list[0] == 'C':
                    row = 2
                if board[row][col-1] != '.':
                    coordinates_input_is_valid = False
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print_board(player_mark, board)
                    print('_ _ _  ARE YOU SURE ?. . . \n')
                    continue
                else:
                    return row, col
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print_board(player_mark, board)
                print('_ _ _  ARE YOU SURE ?. . . \n')
                continue
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print_board(player_mark, board)
            print('_ _ _  ARE YOU SURE ?. . . \n')
            continue


# Function mark() writes the value of player (X or 0) into the row & col element of board.
# It does not do anything if the cell is already marked.
def mark(player_mark, board, coordinates):
    row = coordinates[0]
    col = coordinates[1]
    
    if board[row][col-1] == '.':
        board[row][col-1] = player_mark
    else:
        pass
    

# Function has_won() returns True if player (X or 0) has three of their marks 
# in a horizontal, vertical, or diagonal row on board.
# Boolean variables representing possible win options
# function checks wheater any winning configuration has been made by player,
# finally checks wheater overall won has been done by player, and then
# returning overall state of function has_won() which is boolean
def has_won(player_mark, board):
    
    row1_win = False
    row2_win = False
    row3_win = False
    col1_win = False
    col2_win = False
    col3_win = False
    diagonal1_win = False
    diagonal2_win = False
    
    if (board[0][0] + board[1][0] + board[2][0]) == (3 * str(player_mark)):
        row1_win = True
    elif (board[0][1] + board[1][1] + board[2][1]) == (3 * str(player_mark)):    
        row2_win = True
    elif (board[0][2] + board[1][2] + board[2][2]) == (3 * str(player_mark)):
        row3_win = True
    elif (board[0][0] + board[0][1] + board[0][2]) == (3 * str(player_mark)):
        col1_win = True
    elif (board[1][0] + board[1][1] + board[1][2]) == (3 * str(player_mark)):
        col2_win = True
    elif (board[2][0] + board[2][1] + board[2][2]) == (3 * str(player_mark)):
        col3_win = True
    elif (board[0][0] + board[1][1] + board[2][2]) == (3 * str(player_mark)):
        diagonal1_win = True
    elif (board[0][2] + board[1][1] + board[2][0]) == (3 * str(player_mark)): 
        diagonal2_win = True

    if (row1_win or row2_win or row3_win or col1_win or col2_win or col3_win or diagonal1_win or diagonal2_win) == True:
        player_has_won = True
        print('You WON !')
    else:
        player_has_won = False 
    return player_has_won
    

# function is_full() returns True if there are no empty fields on the board,
# returns False otherwise
def is_full(player_mark, board):
    board_is_full = False
    for x in board:
        for y in x:
            if y == '.':
                board_is_full = False
                return board_is_full
            else:
                board_is_full = True
    return board_is_full


# function print_board() prints current state of board, updated every round
def print_board(player_mark, board):
    print('\n' + '\n')
    print('   1     2     3')
    print('A  ' + str(board[0][0]) + '  ' +'|  ' + str(board[0][1]) + '  ' + '|  ' + str(board[0][2]))
    print('  ' + '----+-----+-----')
    print('B  ' + str(board[1][0]) + '  ' +'|  ' + str(board[1][1]) + '  ' + '|  ' + str(board[1][2]))
    print('  ' + '----+-----+-----')
    print('C  ' + str(board[2][0]) + '  ' +'|  ' + str(board[2][1]) + '  ' + '|  ' + str(board[2][2]))
    print('\n')


# function print_result() stops main game loop, and when it occures prints one of two possible 
# results, win or a tie.
# If one of players win or its a tie, print_results returns True in order to stop main game loop
def print_result(player_mark, player_has_won, board_is_full):
    if player_has_won == True:
        print('Player: " ' + str(player_mark) + ' "  IS THE WINNER !\n')  
        return True
    elif (player_has_won == False) and (board_is_full == True):
        print('LOOKS LIKE WE HAVE A TIE ! --- nobody wins ---\n')
        return True
    else:
        return False


# function tictactoe_game() uses previous functions together and runs a two players game and provide turns, by 
# changing a player sing from 'X' to 'O' in a loop. It also checks, if user 
# wants to quit by typing 'quit' instead of typing coordinates.
def tictactoe_game(board, player_mark):
    player_switch = 1
    print_board(player_mark, board)
    game_is_over = False
    while game_is_over == False:
        if (player_switch % 2 != 0):
            player_mark = 'X'
        elif (player_switch % 2 == 0):
            player_mark = 'O'
        coordinates = get_move()
        if coordinates == ('quit'):
            print("Quitting programm. . .\n\nBYE !\n")
            sys.exit()
        mark(player_mark, board, coordinates)
        os.system('cls' if os.name == 'nt' else 'clear')
        print_board(player_mark, board)
        player_has_won = has_won(player_mark, board)
        board_is_full = is_full(player_mark, board)
        game_is_over = print_result(player_mark, player_has_won, board_is_full)
        player_switch += 1



# main game
board = init_board()
player_mark = ('')
os.system('cls' if os.name == 'nt' else 'clear')
tictactoe_game(board, player_mark)