# START of the programm
# importing modules:
# defining functions:
import sys
import os
import time
os.get_terminal_size()
width = os.get_terminal_size().columns


def main_menu():  
    user_choice_before_game_valid = False
    os.system('cls' if os.name == 'nt' else 'clear')

    print('\n\n\n\n████████╗██╗ ██████╗    ████████╗ █████╗  ██████╗    ████████╗ ██████╗ ███████╗')
    print('╚══██╔══╝██║██╔════╝    ╚══██╔══╝██╔══██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔════╝')
    print('   ██║   ██║██║            ██║   ███████║██║            ██║   ██║   ██║█████╗  ')
    print('   ██║   ██║██║            ██║   ██╔══██║██║            ██║   ██║   ██║██╔══╝  ')
    print('   ██║   ██║╚██████╗       ██║   ██║  ██║╚██████╗       ██║   ╚██████╔╝███████╗')
    print('   ╚═╝   ╚═╝ ╚═════╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝       ╚═╝    ╚═════╝ ╚══════╝\n\n')  
    print('▄█░ ▄ 　 ▒█▀▀█ █░░ █▀▀█ █░░█ █▀▀ █▀▀█ 　 ▀█░█▀ █▀▀ 　 █▀▀█ █░░ █▀▀█ █░░█ █▀▀ █▀▀█')
    print('░█░ ░ 　 ▒█▄▄█ █░░ █▄▄█ █▄▄█ █▀▀ █▄▄▀ 　 ░█▄█░ ▀▀█ 　 █░░█ █░░ █▄▄█ █▄▄█ █▀▀ █▄▄▀')
    print('▄█▄ ▀ 　 ▒█░░░ ▀▀▀ ▀░░▀ ▄▄▄█ ▀▀▀ ▀░▀▀ 　 ░░▀░░ ▀▀▀ 　 █▀▀▀ ▀▀▀ ▀░░▀ ▄▄▄█ ▀▀▀ ▀░▀▀\n\n')
    print('█▀█ ▄ 　 ▒█▀▀█ █░░ █▀▀█ █░░█ █▀▀ █▀▀█ 　 ▀█░█▀ █▀▀ 　 ▒█▀▀█ ▒█▀▀█ ▒█░▒█ ')
    print('░▄▀ ░ 　 ▒█▄▄█ █░░ █▄▄█ █▄▄█ █▀▀ █▄▄▀ 　 ░█▄█░ ▀▀█ 　 ▒█░░░ ▒█▄▄█ ▒█░▒█ ')
    print('█▄▄ ▀ 　 ▒█░░░ ▀▀▀ ▀░░▀ ▄▄▄█ ▀▀▀ ▀░▀▀ 　 ░░▀░░ ▀▀▀ 　 ▒█▄▄█ ▒█░░░ ░▀▄▄▀ \n\n')
    print('█▀▀█ ▄ 　 ▒█▀▀█ █░░█ ░▀░ ▀▀█▀▀ 　 █▀▀▀ █▀▀█ █▀▄▀█ █▀▀ ')
    print('█▄▀█ ░ 　 ▒█░▒█ █░░█ ▀█▀ ░░█░░ 　 █░▀█ █▄▄█ █░▀░█ █▀▀ ')
    print('█▄▄█ ▀ 　 ░▀▀█▄ ░▀▀▀ ▀▀▀ ░░▀░░ 　 ▀▀▀▀ ▀░░▀ ▀░░░▀ ▀▀▀ \n')

    while user_choice_before_game_valid == False:  
        user_choice_before_game = str(input('\nCHOOSE A NUMBER:\n'))
        if (user_choice_before_game == '1') or (user_choice_before_game == '2') or (user_choice_before_game == '0'):
            user_choice_before_game_valid = True
            return user_choice_before_game
        else:
            print('\n- - - TRY AGAIN - - -\n')
            continue


def second_menu():
    user_choice_before_game_valid = False
    os.system('cls' if os.name == 'nt' else 'clear')

    print('▄█░ ▄ 　 █░░█ █░░█ █▀▄▀█ █▀▀█ █▀▀▄ 　 █▀▀ ▀▀█▀▀ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀') 
    print('░█░ ░ 　 █▀▀█ █░░█ █░▀░█ █▄▄█ █░░█ 　 ▀▀█ ░░█░░ █▄▄█ █▄▄▀ ░░█░░ ▀▀█')
    print('▄█▄ ▀ 　 ▀░░▀ ░▀▀▀ ▀░░░▀ ▀░░▀ ▀░░▀ 　 ▀▀▀ ░░▀░░ ▀░░▀ ▀░▀▀ ░░▀░░ ▀▀▀\n')
    print('█▀█ ▄ 　 ▒█▀▀█ ▒█▀▀█ ▒█░▒█ 　 █▀▀ ▀▀█▀▀ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀')
    print('░▄▀ ░ 　 ▒█░░░ ▒█▄▄█ ▒█░▒█ 　 ▀▀█ ░░█░░ █▄▄█ █▄▄▀ ░░█░░ ▀▀█')
    print('█▄▄ ▀ 　 ▒█▄▄█ ▒█░░░ ░▀▄▄▀ 　 ▀▀▀ ░░▀░░ ▀░░▀ ▀░▀▀ ░░▀░░ ▀▀▀\n')

    while user_choice_before_game_valid == False:  
        user_choice_before_game = str(input('\nCHOOSE A NUMBER:\n'))
        if (user_choice_before_game == '1') or (user_choice_before_game == '2'):
            user_choice_before_game_valid = True
            return user_choice_before_game
        else:
            print('\n- - - TRY AGAIN - - -\n')
            continue

def third_menu():
    user_diff_choice_valid = False
    os.system('cls' if os.name == 'nt' else 'clear')

    print('█▀▀▄ ░▀░ █▀▀ █▀▀ ░▀░ █▀▀ █░░█ █░░ ▀▀█▀▀ █░░█ 　 █░░ █▀▀ ▀█░█▀ █▀▀ █░░')
    print('█░░█ ▀█▀ █▀▀ █▀▀ ▀█▀ █░░ █░░█ █░░ ░░█░░ █▄▄█ 　 █░░ █▀▀ ░█▄█░ █▀▀ █░░')
    print('▀▀▀░ ▀▀▀ ▀░░ ▀░░ ▀▀▀ ▀▀▀ ░▀▀▀ ▀▀▀ ░░▀░░ ▄▄▄█ 　 ▀▀▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀▀▀\n')
    print('▄█░ ▄ 　 █▀▀ █▀▀█ █▀▀ █░░█')
    print('░█░ ░ 　 █▀▀ █▄▄█ ▀▀█ █▄▄█')
    print('▄█▄ ▀ 　 ▀▀▀ ▀░░▀ ▀▀▀ ▄▄▄█\n')
    print('█▀█ ▄ 　 █▀▀▄ ░▀░ █▀▀▀ █░░█ ▀▀█▀▀ █▀▄▀█ █▀▀█ █▀▀█ █▀▀')
    print('░▄▀ ░ 　 █░░█ ▀█▀ █░▀█ █▀▀█ ░░█░░ █░▀░█ █▄▄█ █▄▄▀ █▀▀')
    print('█▄▄ ▀ 　 ▀░░▀ ▀▀▀ ▀▀▀▀ ▀░░▀ ░░▀░░ ▀░░░▀ ▀░░▀ ▀░▀▀ ▀▀▀\n')

    while user_diff_choice_valid == False:  
        user_diff_choice = str(input('\nCHOOSE A NUMBER:\n'))
        if (user_diff_choice == '1') or (user_diff_choice == '2'):
            user_diff_choice_valid = True
            user_diff_choice = int(user_diff_choice)
            return user_diff_choice
        else:
            print('\n- - - TRY AGAIN - - -\n')
            continue


def init_board():
    row1 = ['.','.','.']
    row2 = ['.','.','.']
    row3 = ['.','.','.']
    board = [row1, row2, row3]
    return board


# function get_move() asks for user input and returns the coordinates of a valid move on board.
def get_move(player_mark):
    list_of_possible_coordinates_str = ['a', 'A', 'b', 'B', 'c', 'C']
    list_of_possible_coordinates_int = ['1', '2', '3']
    coordinates_input_is_valid = False
    
    # Function is repeating input request until proper input is given.
    # Temporary list is being made here, for keeping user coordinates or quit input for processing.
    while coordinates_input_is_valid == False:
        print(('Player " ' + str(player_mark) + ' "' + ' turn\n').center(width))
        print("Provide VALID coordinates (LETTER + NUMBER, e.g.: A1, C2) \n".center(width))
        print("or type 'Quit' to exit program anytime):\n".center(width))
        coordinates_given_by_user = str(input())
        coordinates_list = []
        os.system('cls' if os.name == 'nt' else 'clear')
        print_board(player_mark, board)
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
                    print('- - - TRY AGAIN - - - \n'.center(width))
                    continue
                else:
                    return row, col
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print_board(player_mark, board)
                print('- - - TRY AGAIN - - - \n'.center(width))
                continue
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print_board(player_mark, board)
            print('- - - TRY AGAIN - - - \n'.center(width))
            continue


def get_ai_move(board, player_mark, cpu_or_human_starts, player_switch, difficulty_level):

    if (difficulty_level == 2) or (difficulty_level == 1):
        if cpu_or_human_starts == 'HUMAN-AI':

            if player_switch == 2:
                if (board[0][0] == 'X') or (board[0][2] == 'X') or (board[2][0] == 'X') or (board[2][2] == 'X'): 
                    coordinates_given_by_cpu = (1, 2)
                    return coordinates_given_by_cpu
                elif board[2][0] == '.':
                    coordinates_given_by_cpu = (2, 1)
                    return coordinates_given_by_cpu 

            if player_switch == 4:
                if (board[2][0] == 'X') and (board[0][2] == 'X'):
                    coordinates_given_by_cpu = (1, 1)
                    return coordinates_given_by_cpu
                elif (board[0][0] == 'X') and (board[2][2] == 'X'):
                    coordinates_given_by_cpu = (0, 2)
                    return coordinates_given_by_cpu
                #prevent easy loose
                if ((board[1][1] == 'X') and (board[2][1] == 'X') and (board[0][1] == '.')) or ((board[0][0] == 'X') and (board[0][2] == 'X') and (board[0][1] == '.')):
                    coordinates_given_by_cpu = (0, 2)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'X') and (board[2][0] == 'X') and (board[1][0] == '.')) or ((board[1][1] == 'X') and (board[1][2] == 'X') and (board[1][0] == '.')):
                    coordinates_given_by_cpu = (1, 1)
                    return coordinates_given_by_cpu
                if ((board[1][0] == 'X') and (board[1][1] == 'X') and (board[1][2] == '.')) or ((board[0][2] == 'X') and (board[2][2] == 'X') and (board[1][2] == '.')):
                    coordinates_given_by_cpu = (1, 3)
                    return coordinates_given_by_cpu
                if ((board[0][1] == 'X') and (board[1][1] == 'X') and (board[2][1] == '.')) or ((board[2][0] == 'X') and (board[2][2] == 'X') and (board[2][1] == '.')):
                    coordinates_given_by_cpu = (2, 2)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'X') and (board[2][2] == 'X') and (board[1][1] == '.')) or ((board[2][0] == 'X') and (board[0][2] == 'X') and (board[1][1] == '.')) or ((board[1][0] == 'X') and (board[1][2] == 'X') and (board[1][1] == '.')) or ((board[0][1] == 'X') and (board[2][1] == 'X') and (board[1][1] == '.')):
                    coordinates_given_by_cpu = (1, 2)
                    return coordinates_given_by_cpu
                if ((board[2][0] == 'X') and (board[1][1] == 'X') and (board[0][2] == '.')) or ((board[0][0] == 'X') and (board[0][1] == 'X') and (board[0][2] == '.')) or ((board[1][2] == 'X') and (board[2][2] == 'X') and (board[0][2] == '.')):
                    coordinates_given_by_cpu = (0, 3)
                    return coordinates_given_by_cpu
                if ((board[1][1] == 'X') and (board[2][2] == 'X') and (board[0][0] == '.')) or ((board[1][0] == 'X') and (board[2][0] == 'X') and (board[0][0] == '.')) or ((board[0][1] == 'X') and (board[0][2] == 'X') and (board[0][0] == '.')):
                    coordinates_given_by_cpu = (0, 1)
                    return coordinates_given_by_cpu
                if ((board[0][2] == 'X') and (board[1][2] == 'X') and (board[2][2] == '.')) or ((board[2][0] == 'X') and (board[2][1] == 'X') and (board[2][2] == '.')) or ((board[0][0] == 'X') and (board[1][1] == 'X') and (board[2][2] == '.')):
                    coordinates_given_by_cpu = (2, 3)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'X') and (board[1][0] == 'X') and (board[2][0] == '.')) or ((board[1][1] == 'X') and (board[0][2] == 'X') and (board[2][0] == '.')) or ((board[2][1] == 'X') and (board[2][2] == 'X') and (board[2][0] == '.')):
                    coordinates_given_by_cpu = (2, 1)
                    return coordinates_given_by_cpu
                # cpu goes on non occupied edge with second move
                elif board[0][1] == '.':
                    coordinates_given_by_cpu = (0, 2)
                    return coordinates_given_by_cpu
                elif board[1][2] == '.':
                    coordinates_given_by_cpu = (1, 3)
                    return coordinates_given_by_cpu
                elif board[2][1] == '.':
                    coordinates_given_by_cpu = (2, 2)
                    return coordinates_given_by_cpu
                elif board[1][0] == '.':
                    coordinates_given_by_cpu = (1, 1)
                    return coordinates_given_by_cpu

            if player_switch == 6:
                #try to win
                if ((board[1][1] == 'O') and (board[2][1] == 'O') and (board[0][1] == '.')) or ((board[0][0] == 'O') and (board[0][2] == 'O') and (board[0][1] == '.')):
                    coordinates_given_by_cpu = (0, 2)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'O') and (board[2][0] == 'O') and (board[1][0] == '.')) or ((board[1][1] == 'O') and (board[1][2] == 'O') and (board[1][0] == '.')):
                    coordinates_given_by_cpu = (1, 1)
                    return coordinates_given_by_cpu
                if ((board[1][0] == 'O') and (board[1][1] == 'O') and (board[1][2] == '.')) or ((board[0][2] == 'O') and (board[2][2] == 'O') and (board[1][2] == '.')):
                    coordinates_given_by_cpu = (1, 3)
                    return coordinates_given_by_cpu
                if ((board[0][1] == 'O') and (board[1][1] == 'O') and (board[2][1] == '.')) or ((board[2][0] == 'O') and (board[2][2] == 'O') and (board[2][1] == '.')):
                    coordinates_given_by_cpu = (2, 2)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'O') and (board[2][2] == 'O') and (board[1][1] == '.')) or ((board[2][0] == 'O') and (board[0][2] == 'O') and (board[1][1] == '.')) or ((board[1][0] == 'O') and (board[1][2] == 'O') and (board[1][1] == '.')) or ((board[0][1] == 'O') and (board[2][1] == 'O') and (board[1][1] == '.')):
                    coordinates_given_by_cpu = (1, 2)
                    return coordinates_given_by_cpu
                if ((board[2][0] == 'O') and (board[1][1] == 'O') and (board[0][2] == '.')) or ((board[0][0] == 'O') and (board[0][1] == 'O') and (board[0][2] == '.')) or ((board[1][2] == 'O') and (board[2][2] == 'O') and (board[0][2] == '.')):
                    coordinates_given_by_cpu = (0, 3)
                    return coordinates_given_by_cpu
                if ((board[1][1] == 'O') and (board[2][2] == 'O') and (board[0][0] == '.')) or ((board[1][0] == 'O') and (board[2][0] == 'O') and (board[0][0] == '.')) or ((board[0][1] == 'O') and (board[0][2] == 'O') and (board[0][0] == '.')):
                    coordinates_given_by_cpu = (0, 1)
                    return coordinates_given_by_cpu
                if ((board[0][2] == 'O') and (board[1][2] == 'O') and (board[2][2] == '.')) or ((board[2][0] == 'O') and (board[2][1] == 'O') and (board[2][2] == '.')) or ((board[0][0] == 'O') and (board[1][1] == 'O') and (board[2][2] == '.')):
                    coordinates_given_by_cpu = (2, 3)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'O') and (board[1][0] == 'O') and (board[2][0] == '.')) or ((board[1][1] == 'O') and (board[0][2] == 'O') and (board[2][0] == '.')) or ((board[2][1] == 'O') and (board[2][2] == 'O') and (board[2][0] == '.')):
                    coordinates_given_by_cpu = (2, 1)
                    return coordinates_given_by_cpu
                #prevent easy loose
                if ((board[1][1] == 'X') and (board[2][1] == 'X') and (board[0][1] == '.')) or ((board[0][0] == 'X') and (board[0][2] == 'X') and (board[0][1] == '.')):
                    coordinates_given_by_cpu = (0, 2)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'X') and (board[2][0] == 'X') and (board[1][0] == '.')) or ((board[1][1] == 'X') and (board[1][2] == 'X') and (board[1][0] == '.')):
                    coordinates_given_by_cpu = (1, 1)
                    return coordinates_given_by_cpu
                if ((board[1][0] == 'X') and (board[1][1] == 'X') and (board[1][2] == '.')) or ((board[0][2] == 'X') and (board[2][2] == 'X') and (board[1][2] == '.')):
                    coordinates_given_by_cpu = (1, 3)
                    return coordinates_given_by_cpu
                if ((board[0][1] == 'X') and (board[1][1] == 'X') and (board[2][1] == '.')) or ((board[2][0] == 'X') and (board[2][2] == 'X') and (board[2][1] == '.')):
                    coordinates_given_by_cpu = (2, 2)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'X') and (board[2][2] == 'X') and (board[1][1] == '.')) or ((board[2][0] == 'X') and (board[0][2] == 'X') and (board[1][1] == '.')) or ((board[1][0] == 'X') and (board[1][2] == 'X') and (board[1][1] == '.')) or ((board[0][1] == 'X') and (board[2][1] == 'X') and (board[1][1] == '.')):
                    coordinates_given_by_cpu = (1, 2)
                    return coordinates_given_by_cpu
                if ((board[2][0] == 'X') and (board[1][1] == 'X') and (board[0][2] == '.')) or ((board[0][0] == 'X') and (board[0][1] == 'X') and (board[0][2] == '.')) or ((board[1][2] == 'X') and (board[2][2] == 'X') and (board[0][2] == '.')):
                    coordinates_given_by_cpu = (0, 3)
                    return coordinates_given_by_cpu
                if ((board[1][1] == 'X') and (board[2][2] == 'X') and (board[0][0] == '.')) or ((board[1][0] == 'X') and (board[2][0] == 'X') and (board[0][0] == '.')) or ((board[0][1] == 'X') and (board[0][2] == 'X') and (board[0][0] == '.')):
                    coordinates_given_by_cpu = (0, 1)
                    return coordinates_given_by_cpu
                if ((board[0][2] == 'X') and (board[1][2] == 'X') and (board[2][2] == '.')) or ((board[2][0] == 'X') and (board[2][1] == 'X') and (board[2][2] == '.')) or ((board[0][0] == 'X') and (board[1][1] == 'X') and (board[2][2] == '.')):
                    coordinates_given_by_cpu = (2, 3)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'X') and (board[1][0] == 'X') and (board[2][0] == '.')) or ((board[1][1] == 'X') and (board[0][2] == 'X') and (board[2][0] == '.')) or ((board[2][1] == 'X') and (board[2][2] == 'X') and (board[2][0] == '.')):
                    coordinates_given_by_cpu = (2, 1)
                    return coordinates_given_by_cpu
                # if player blocks
                if (board[1][0] == 'X') and (board[1][1] == 'O') and (board[1][2] == 'O'):
                    coordinates_given_by_cpu = (0, 2)
                    return coordinates_given_by_cpu
                if (board[0][1] == 'X') and (board[1][1] == 'O') and (board[2][1] == 'O'):
                    coordinates_given_by_cpu = (1, 3)
                    return coordinates_given_by_cpu
                if (board[1][2] == 'X') and (board[1][1] == 'O') and (board[1][0] == 'O'):
                    coordinates_given_by_cpu = (2, 2)
                    return coordinates_given_by_cpu
                if (board[2][1] == 'X') and (board[1][1] == 'O') and (board[0][1] == 'O'):
                    coordinates_given_by_cpu = (1, 1)
                    return coordinates_given_by_cpu
                    
            if player_switch == 8:
                #try to win
                if ((board[1][1] == 'O') and (board[2][1] == 'O') and (board[0][1] == '.')) or ((board[0][0] == 'O') and (board[0][2] == 'O') and (board[0][1] == '.')):
                    coordinates_given_by_cpu = (0, 2)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'O') and (board[2][0] == 'O') and (board[1][0] == '.')) or ((board[1][1] == 'O') and (board[1][2] == 'O') and (board[1][0] == '.')):
                    coordinates_given_by_cpu = (1, 1)
                    return coordinates_given_by_cpu
                if ((board[1][0] == 'O') and (board[1][1] == 'O') and (board[1][2] == '.')) or ((board[0][2] == 'O') and (board[2][2] == 'O') and (board[1][2] == '.')):
                    coordinates_given_by_cpu = (1, 3)
                    return coordinates_given_by_cpu
                if ((board[0][1] == 'O') and (board[1][1] == 'O') and (board[2][1] == '.')) or ((board[2][0] == 'O') and (board[2][2] == 'O') and (board[2][1] == '.')):
                    coordinates_given_by_cpu = (2, 2)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'O') and (board[2][2] == 'O') and (board[1][1] == '.')) or ((board[2][0] == 'O') and (board[0][2] == 'O') and (board[1][1] == '.')) or ((board[1][0] == 'O') and (board[1][2] == 'O') and (board[1][1] == '.')) or ((board[0][1] == 'O') and (board[2][1] == 'O') and (board[1][1] == '.')):
                    coordinates_given_by_cpu = (1, 2)
                    return coordinates_given_by_cpu
                if ((board[2][0] == 'O') and (board[1][1] == 'O') and (board[0][2] == '.')) or ((board[0][0] == 'O') and (board[0][1] == 'O') and (board[0][2] == '.')) or ((board[1][2] == 'O') and (board[2][2] == 'O') and (board[0][2] == '.')):
                    coordinates_given_by_cpu = (0, 3)
                    return coordinates_given_by_cpu
                if ((board[1][1] == 'O') and (board[2][2] == 'O') and (board[0][0] == '.')) or ((board[1][0] == 'O') and (board[2][0] == 'O') and (board[0][0] == '.')) or ((board[0][1] == 'O') and (board[0][2] == 'O') and (board[0][0] == '.')):
                    coordinates_given_by_cpu = (0, 1)
                    return coordinates_given_by_cpu
                if ((board[0][2] == 'O') and (board[1][2] == 'O') and (board[2][2] == '.')) or ((board[2][0] == 'O') and (board[2][1] == 'O') and (board[2][2] == '.')) or ((board[0][0] == 'O') and (board[1][1] == 'O') and (board[2][2] == '.')):
                    coordinates_given_by_cpu = (2, 3)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'O') and (board[1][0] == 'O') and (board[2][0] == '.')) or ((board[1][1] == 'O') and (board[0][2] == 'O') and (board[2][0] == '.')) or ((board[2][1] == 'O') and (board[2][2] == 'O') and (board[2][0] == '.')):
                    coordinates_given_by_cpu = (2, 1)
                    return coordinates_given_by_cpu
                #prevent easy loose
                if ((board[1][1] == 'X') and (board[2][1] == 'X') and (board[0][1] == '.')) or ((board[0][0] == 'X') and (board[0][2] == 'X') and (board[0][1] == '.')):
                    coordinates_given_by_cpu = (0, 2)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'X') and (board[2][0] == 'X') and (board[1][0] == '.')) or ((board[1][1] == 'X') and (board[1][2] == 'X') and (board[1][0] == '.')):
                    coordinates_given_by_cpu = (1, 1)
                    return coordinates_given_by_cpu
                if ((board[1][0] == 'X') and (board[1][1] == 'X') and (board[1][2] == '.')) or ((board[0][2] == 'X') and (board[2][2] == 'X') and (board[1][2] == '.')):
                    coordinates_given_by_cpu = (1, 3)
                    return coordinates_given_by_cpu
                if ((board[0][1] == 'X') and (board[1][1] == 'X') and (board[2][1] == '.')) or ((board[2][0] == 'X') and (board[2][2] == 'X') and (board[2][1] == '.')):
                    coordinates_given_by_cpu = (2, 2)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'X') and (board[2][2] == 'X') and (board[1][1] == '.')) or ((board[2][0] == 'X') and (board[0][2] == 'X') and (board[1][1] == '.')) or ((board[1][0] == 'X') and (board[1][2] == 'X') and (board[1][1] == '.')) or ((board[0][1] == 'X') and (board[2][1] == 'X') and (board[1][1] == '.')):
                    coordinates_given_by_cpu = (1, 2)
                    return coordinates_given_by_cpu
                if ((board[2][0] == 'X') and (board[1][1] == 'X') and (board[0][2] == '.')) or ((board[0][0] == 'X') and (board[0][1] == 'X') and (board[0][2] == '.')) or ((board[1][2] == 'X') and (board[2][2] == 'X') and (board[0][2] == '.')):
                    coordinates_given_by_cpu = (0, 3)
                    return coordinates_given_by_cpu
                if ((board[1][1] == 'X') and (board[2][2] == 'X') and (board[0][0] == '.')) or ((board[1][0] == 'X') and (board[2][0] == 'X') and (board[0][0] == '.')) or ((board[0][1] == 'X') and (board[0][2] == 'X') and (board[0][0] == '.')):
                    coordinates_given_by_cpu = (0, 1)
                    return coordinates_given_by_cpu
                if ((board[0][2] == 'X') and (board[1][2] == 'X') and (board[2][2] == '.')) or ((board[2][0] == 'X') and (board[2][1] == 'X') and (board[2][2] == '.')) or ((board[0][0] == 'X') and (board[1][1] == 'X') and (board[2][2] == '.')):
                    coordinates_given_by_cpu = (2, 3)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'X') and (board[1][0] == 'X') and (board[2][0] == '.')) or ((board[1][1] == 'X') and (board[0][2] == 'X') and (board[2][0] == '.')) or ((board[2][1] == 'X') and (board[2][2] == 'X') and (board[2][0] == '.')):
                    coordinates_given_by_cpu = (2, 1)
                    return coordinates_given_by_cpu
                else:
                    for row in range(0, 3):
                        for col in range(0, 3):
                            if board[row][col] == '.':
                                coordinates_given_by_cpu = ((row), (col + 1))
                                return coordinates_given_by_cpu   

            if player_switch == 10:
                #try to win
                if ((board[1][1] == 'O') and (board[2][1] == 'O') and (board[0][1] == '.')) or ((board[0][0] == 'O') and (board[0][2] == 'O') and (board[0][1] == '.')):
                    coordinates_given_by_cpu = (0, 2)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'O') and (board[2][0] == 'O') and (board[1][0] == '.')) or ((board[1][1] == 'O') and (board[1][2] == 'O') and (board[1][0] == '.')):
                    coordinates_given_by_cpu = (1, 1)
                    return coordinates_given_by_cpu
                if ((board[1][0] == 'O') and (board[1][1] == 'O') and (board[1][2] == '.')) or ((board[0][2] == 'O') and (board[2][2] == 'O') and (board[1][2] == '.')):
                    coordinates_given_by_cpu = (1, 3)
                    return coordinates_given_by_cpu
                if ((board[0][1] == 'O') and (board[1][1] == 'O') and (board[2][1] == '.')) or ((board[2][0] == 'O') and (board[2][2] == 'O') and (board[2][1] == '.')):
                    coordinates_given_by_cpu = (2, 2)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'O') and (board[2][2] == 'O') and (board[1][1] == '.')) or ((board[2][0] == 'O') and (board[0][2] == 'O') and (board[1][1] == '.')) or ((board[1][0] == 'O') and (board[1][2] == 'O') and (board[1][1] == '.')) or ((board[0][1] == 'O') and (board[2][1] == 'O') and (board[1][1] == '.')):
                    coordinates_given_by_cpu = (1, 2)
                    return coordinates_given_by_cpu
                if ((board[2][0] == 'O') and (board[1][1] == 'O') and (board[0][2] == '.')) or ((board[0][0] == 'O') and (board[0][1] == 'O') and (board[0][2] == '.')) or ((board[1][2] == 'O') and (board[2][2] == 'O') and (board[0][2] == '.')):
                    coordinates_given_by_cpu = (0, 3)
                    return coordinates_given_by_cpu
                if ((board[1][1] == 'O') and (board[2][2] == 'O') and (board[0][0] == '.')) or ((board[1][0] == 'O') and (board[2][0] == 'O') and (board[0][0] == '.')) or ((board[0][1] == 'O') and (board[0][2] == 'O') and (board[0][0] == '.')):
                    coordinates_given_by_cpu = (0, 1)
                    return coordinates_given_by_cpu
                if ((board[0][2] == 'O') and (board[1][2] == 'O') and (board[2][2] == '.')) or ((board[2][0] == 'O') and (board[2][1] == 'O') and (board[2][2] == '.')) or ((board[0][0] == 'O') and (board[1][1] == 'O') and (board[2][2] == '.')):
                    coordinates_given_by_cpu = (2, 3)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'O') and (board[1][0] == 'O') and (board[2][0] == '.')) or ((board[1][1] == 'O') and (board[0][2] == 'O') and (board[2][0] == '.')) or ((board[2][1] == 'O') and (board[2][2] == 'O') and (board[2][0] == '.')):
                    coordinates_given_by_cpu = (2, 1)
                    return coordinates_given_by_cpu
                #prevent easy loose
                if ((board[1][1] == 'X') and (board[2][1] == 'X') and (board[0][1] == '.')) or ((board[0][0] == 'X') and (board[0][2] == 'X') and (board[0][1] == '.')):
                    coordinates_given_by_cpu = (0, 2)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'X') and (board[2][0] == 'X') and (board[1][0] == '.')) or ((board[1][1] == 'X') and (board[1][2] == 'X') and (board[1][0] == '.')):
                    coordinates_given_by_cpu = (1, 1)
                    return coordinates_given_by_cpu
                if ((board[1][0] == 'X') and (board[1][1] == 'X') and (board[1][2] == '.')) or ((board[0][2] == 'X') and (board[2][2] == 'X') and (board[1][2] == '.')):
                    coordinates_given_by_cpu = (1, 3)
                    return coordinates_given_by_cpu
                if ((board[0][1] == 'X') and (board[1][1] == 'X') and (board[2][1] == '.')) or ((board[2][0] == 'X') and (board[2][2] == 'X') and (board[2][1] == '.')):
                    coordinates_given_by_cpu = (2, 2)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'X') and (board[2][2] == 'X') and (board[1][1] == '.')) or ((board[2][0] == 'X') and (board[0][2] == 'X') and (board[1][1] == '.')) or ((board[1][0] == 'X') and (board[1][2] == 'X') and (board[1][1] == '.')) or ((board[0][1] == 'X') and (board[2][1] == 'X') and (board[1][1] == '.')):
                    coordinates_given_by_cpu = (1, 2)
                    return coordinates_given_by_cpu
                if ((board[2][0] == 'X') and (board[1][1] == 'X') and (board[0][2] == '.')) or ((board[0][0] == 'X') and (board[0][1] == 'X') and (board[0][2] == '.')) or ((board[1][2] == 'X') and (board[2][2] == 'X') and (board[0][2] == '.')):
                    coordinates_given_by_cpu = (0, 3)
                    return coordinates_given_by_cpu
                if ((board[1][1] == 'X') and (board[2][2] == 'X') and (board[0][0] == '.')) or ((board[1][0] == 'X') and (board[2][0] == 'X') and (board[0][0] == '.')) or ((board[0][1] == 'X') and (board[0][2] == 'X') and (board[0][0] == '.')):
                    coordinates_given_by_cpu = (0, 1)
                    return coordinates_given_by_cpu
                if ((board[0][2] == 'X') and (board[1][2] == 'X') and (board[2][2] == '.')) or ((board[2][0] == 'X') and (board[2][1] == 'X') and (board[2][2] == '.')) or ((board[0][0] == 'X') and (board[1][1] == 'X') and (board[2][2] == '.')):
                    coordinates_given_by_cpu = (2, 3)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'X') and (board[1][0] == 'X') and (board[2][0] == '.')) or ((board[1][1] == 'X') and (board[0][2] == 'X') and (board[2][0] == '.')) or ((board[2][1] == 'X') and (board[2][2] == 'X') and (board[2][0] == '.')):
                    coordinates_given_by_cpu = (2, 1)
                    return coordinates_given_by_cpu
                else:
                    for row in range(0, 3):
                        for col in range(0, 3):
                            if board[row][col] == '.':
                                coordinates_given_by_cpu = ((row), (col + 1))
                                return coordinates_given_by_cpu
            
        if cpu_or_human_starts == 'AI-HUMAN':

            # round 1
            if player_switch == 1:
                coordinates_given_by_cpu = (2, 1)
                return coordinates_given_by_cpu
            # round 2
            if player_switch == 3:
                #jeśli player położył na środku
                if board[1][1] == 'O':
                    if board[0][2] == '.':
                        coordinates_given_by_cpu = (0, 3)
                        return coordinates_given_by_cpu
                #jeśli nie na środku to cpu robi prawo dół, lub do góry 
                elif (board[0][0] == 'O') or (board[1][0] == 'O') or (board[0][2] == 'O') or (board[1][2] == 'O'):
                    coordinates_given_by_cpu = (2, 3)
                    return coordinates_given_by_cpu
                elif (board[0][1] == 'O') or (board[2][2] == 'O') or (board[2][1] == 'O'):
                    coordinates_given_by_cpu = (0, 1)
                    return coordinates_given_by_cpu

            #round 3        
            if player_switch == 5:
                #jeśli dał na środek, a potem w róg, daj w wolny róg
                if ((board[0][0] == 'O') or (board[2][2] == 'O')) and (board[1][1] == 'O'):
                    if board[0][0] == '.':
                        coordinates_given_by_cpu = (0, 1)
                        return coordinates_given_by_cpu 
                    elif board[2][2] == '.':
                        coordinates_given_by_cpu = (2, 3)
                        return coordinates_given_by_cpu
                # jesli player nie zablokuje, wygra cpu
                # try to win
                if ((board[1][1] == 'X') and (board[2][1] == 'X') and (board[0][1] == '.')) or ((board[0][0] == 'X') and (board[0][2] == 'X') and (board[0][1] == '.')):
                    coordinates_given_by_cpu = (0, 2)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'X') and (board[2][0] == 'X') and (board[1][0] == '.')) or ((board[1][1] == 'X') and (board[1][2] == 'X') and (board[1][0] == '.')):
                    coordinates_given_by_cpu = (1, 1)
                    return coordinates_given_by_cpu
                if ((board[1][0] == 'X') and (board[1][1] == 'X') and (board[1][2] == '.')) or ((board[0][2] == 'X') and (board[2][2] == 'X') and (board[1][2] == '.')):
                    coordinates_given_by_cpu = (1, 3)
                    return coordinates_given_by_cpu
                if ((board[0][1] == 'X') and (board[1][1] == 'X') and (board[2][1] == '.')) or ((board[2][0] == 'X') and (board[2][2] == 'X') and (board[2][1] == '.')):
                    coordinates_given_by_cpu = (2, 2)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'X') and (board[2][2] == 'X') and (board[1][1] == '.')) or ((board[2][0] == 'X') and (board[0][2] == 'X') and (board[1][1] == '.')) or ((board[1][0] == 'X') and (board[1][2] == 'X') and (board[1][1] == '.')) or ((board[0][1] == 'X') and (board[2][1] == 'X') and (board[1][1] == '.')):
                    coordinates_given_by_cpu = (1, 2)
                    return coordinates_given_by_cpu
                if ((board[2][0] == 'X') and (board[1][1] == 'X') and (board[0][2] == '.')) or ((board[0][0] == 'X') and (board[0][1] == 'X') and (board[0][2] == '.')) or ((board[1][2] == 'X') and (board[2][2] == 'X') and (board[0][2] == '.')):
                    coordinates_given_by_cpu = (0, 3)
                    return coordinates_given_by_cpu
                if ((board[1][1] == 'X') and (board[2][2] == 'X') and (board[0][0] == '.')) or ((board[1][0] == 'X') and (board[2][0] == 'X') and (board[0][0] == '.')) or ((board[0][1] == 'X') and (board[0][2] == 'X') and (board[0][0] == '.')):
                    coordinates_given_by_cpu = (0, 1)
                    return coordinates_given_by_cpu
                if ((board[0][2] == 'X') and (board[1][2] == 'X') and (board[2][2] == '.')) or ((board[2][0] == 'X') and (board[2][1] == 'X') and (board[2][2] == '.')) or ((board[0][0] == 'X') and (board[1][1] == 'X') and (board[2][2] == '.')):
                    coordinates_given_by_cpu = (2, 3)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'X') and (board[1][0] == 'X') and (board[2][0] == '.')) or ((board[1][1] == 'X') and (board[0][2] == 'X') and (board[2][0] == '.')) or ((board[2][1] == 'X') and (board[2][2] == 'X') and (board[2][0] == '.')):
                    coordinates_given_by_cpu = (2, 1)
                    return coordinates_given_by_cpu
                #jesli zablokuje
                elif (board[2][1] == 'O') and (board[0][0] == 'O'):
                    coordinates_given_by_cpu = (0, 3)
                    return coordinates_given_by_cpu
                elif (board[2][1] == 'O') and (board[1][0] == 'O'):
                    coordinates_given_by_cpu = (0, 3)
                    return coordinates_given_by_cpu
                elif (board[2][1] == 'O') and (board[0][2] == 'O'):
                    coordinates_given_by_cpu = (0, 1)
                    return coordinates_given_by_cpu
                elif (board[2][1] == 'O') and (board[1][2] == 'O'):
                    coordinates_given_by_cpu = (0, 1)
                    return coordinates_given_by_cpu
                elif (board[1][0] == 'O') and (board[0][1] == 'O'):
                    coordinates_given_by_cpu = (2, 3)
                    return coordinates_given_by_cpu
                elif (board[1][0] == 'O') and (board[2][1] == 'O'):
                    coordinates_given_by_cpu = (0, 3)
                    return coordinates_given_by_cpu
                elif (board[1][0] == 'O') and (board[2][2] == 'O'):
                    coordinates_given_by_cpu = (0, 3)
                    return coordinates_given_by_cpu
                #prevent easy loose
                if ((board[1][1] == 'O') and (board[2][1] == 'O') and (board[0][1] == '.')) or ((board[0][0] == 'O') and (board[0][2] == 'O') and (board[0][1] == '.')):
                    coordinates_given_by_cpu = (0, 2)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'O') and (board[2][0] == 'O') and (board[1][0] == '.')) or ((board[1][1] == 'O') and (board[1][2] == 'O') and (board[1][0] == '.')):
                    coordinates_given_by_cpu = (1, 1)
                    return coordinates_given_by_cpu
                if ((board[1][0] == 'O') and (board[1][1] == 'O') and (board[1][2] == '.')) or ((board[0][2] == 'O') and (board[2][2] == 'O') and (board[1][2] == '.')):
                    coordinates_given_by_cpu = (1, 3)
                    return coordinates_given_by_cpu
                if ((board[0][1] == 'O') and (board[1][1] == 'O') and (board[2][1] == '.')) or ((board[2][0] == 'O') and (board[2][2] == 'O') and (board[2][1] == '.')):
                    coordinates_given_by_cpu = (2, 2)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'O') and (board[2][2] == 'O') and (board[1][1] == '.')) or ((board[2][0] == 'O') and (board[0][2] == 'O') and (board[1][1] == '.')) or ((board[1][0] == 'O') and (board[1][2] == 'O') and (board[1][1] == '.')) or ((board[0][1] == 'O') and (board[2][1] == 'O') and (board[1][1] == '.')):
                    coordinates_given_by_cpu = (1, 2)
                    return coordinates_given_by_cpu
                if ((board[2][0] == 'O') and (board[1][1] == 'O') and (board[0][2] == '.')) or ((board[0][0] == 'O') and (board[0][1] == 'O') and (board[0][2] == '.')) or ((board[1][2] == 'O') and (board[2][2] == 'O') and (board[0][2] == '.')):
                    coordinates_given_by_cpu = (0, 3)
                    return coordinates_given_by_cpu
                if ((board[1][1] == 'O') and (board[2][2] == 'O') and (board[0][0] == '.')) or ((board[1][0] == 'O') and (board[2][0] == 'O') and (board[0][0] == '.')) or ((board[0][1] == 'O') and (board[0][2] == 'O') and (board[0][0] == '.')):
                    coordinates_given_by_cpu = (0, 1)
                    return coordinates_given_by_cpu
                if ((board[0][2] == 'O') and (board[1][2] == 'O') and (board[2][2] == '.')) or ((board[2][0] == 'O') and (board[2][1] == 'O') and (board[2][2] == '.')) or ((board[0][0] == 'O') and (board[1][1] == 'O') and (board[2][2] == '.')):
                    coordinates_given_by_cpu = (2, 3)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'O') and (board[1][0] == 'O') and (board[2][0] == '.')) or ((board[1][1] == 'O') and (board[0][2] == 'O') and (board[2][0] == '.')) or ((board[2][1] == 'O') and (board[2][2] == 'O') and (board[2][0] == '.')):
                    coordinates_given_by_cpu = (2, 1)
                    return coordinates_given_by_cpu

            # round 4
            if player_switch == 7:
                #player ma możliwość bloków ale przegrał
                if (board[0][0] == 'X') and (board[0][1] == '.') and (board[0][2] == 'X'):
                    coordinates_given_by_cpu = (0, 2)
                    return coordinates_given_by_cpu
                if (board[0][0] == 'X') and (board[1][1] == '.') and (board[2][2] == 'X'):
                    coordinates_given_by_cpu = (1, 2)
                    return coordinates_given_by_cpu
                if (board[0][0] == 'X') and (board[1][0] == '.') and (board[2][0] == 'X'):
                    coordinates_given_by_cpu = (1, 1)
                    return coordinates_given_by_cpu
                if (board[0][2] == 'X') and (board[1][2] == '.') and (board[2][2] == 'X'):
                    coordinates_given_by_cpu = (1, 3)
                    return coordinates_given_by_cpu
                if (board[0][2] == 'X') and (board[1][1] == '.') and (board[2][0] == 'X'):
                    coordinates_given_by_cpu = (1, 2)
                    return coordinates_given_by_cpu
                if (board[0][2] == 'X') and (board[0][1] == '.') and (board[0][0] == 'X'):
                    coordinates_given_by_cpu = (0, 2)
                    return coordinates_given_by_cpu
                
                #prevent easy loose
                if ((board[1][1] == 'O') and (board[2][1] == 'O') and (board[0][1] == '.')) or ((board[0][0] == 'O') and (board[0][2] == 'O') and (board[0][1] == '.')):
                    coordinates_given_by_cpu = (0, 2)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'O') and (board[2][0] == 'O') and (board[1][0] == '.')) or ((board[1][1] == 'O') and (board[1][2] == 'O') and (board[1][0] == '.')):
                    coordinates_given_by_cpu = (1, 1)
                    return coordinates_given_by_cpu
                if ((board[1][0] == 'O') and (board[1][1] == 'O') and (board[1][2] == '.')) or ((board[0][2] == 'O') and (board[2][2] == 'O') and (board[1][2] == '.')):
                    coordinates_given_by_cpu = (1, 3)
                    return coordinates_given_by_cpu
                if ((board[0][1] == 'O') and (board[1][1] == 'O') and (board[2][1] == '.')) or ((board[2][0] == 'O') and (board[2][2] == 'O') and (board[2][1] == '.')):
                    coordinates_given_by_cpu = (2, 2)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'O') and (board[2][2] == 'O') and (board[1][1] == '.')) or ((board[2][0] == 'O') and (board[0][2] == 'O') and (board[1][1] == '.')) or ((board[1][0] == 'O') and (board[1][2] == 'O') and (board[1][1] == '.')) or ((board[0][1] == 'O') and (board[2][1] == 'O') and (board[1][1] == '.')):
                    coordinates_given_by_cpu = (1, 2)
                    return coordinates_given_by_cpu
                if ((board[2][0] == 'O') and (board[1][1] == 'O') and (board[0][2] == '.')) or ((board[0][0] == 'O') and (board[0][1] == 'O') and (board[0][2] == '.')) or ((board[1][2] == 'O') and (board[2][2] == 'O') and (board[0][2] == '.')):
                    coordinates_given_by_cpu = (0, 3)
                    return coordinates_given_by_cpu
                if ((board[1][1] == 'O') and (board[2][2] == 'O') and (board[0][0] == '.')) or ((board[1][0] == 'O') and (board[2][0] == 'O') and (board[0][0] == '.')) or ((board[0][1] == 'O') and (board[0][2] == 'O') and (board[0][0] == '.')):
                    coordinates_given_by_cpu = (0, 1)
                    return coordinates_given_by_cpu
                if ((board[0][2] == 'O') and (board[1][2] == 'O') and (board[2][2] == '.')) or ((board[2][0] == 'O') and (board[2][1] == 'O') and (board[2][2] == '.')) or ((board[0][0] == 'O') and (board[1][1] == 'O') and (board[2][2] == '.')):
                    coordinates_given_by_cpu = (2, 3)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'O') and (board[1][0] == 'O') and (board[2][0] == '.')) or ((board[1][1] == 'O') and (board[0][2] == 'O') and (board[2][0] == '.')) or ((board[2][1] == 'O') and (board[2][2] == 'O') and (board[2][0] == '.')):
                    coordinates_given_by_cpu = (2, 1)
                    return coordinates_given_by_cpu
                if (board[2][0] == 'X') and (board[2][1] == '.') and (board[2][2] == 'X'):
                    coordinates_given_by_cpu = (2, 2)
                    return coordinates_given_by_cpu
                    
            #round 5
            if player_switch == 9: 
                #prevent easy loose
                if ((board[1][1] == 'O') and (board[2][1] == 'O') and (board[0][1] == '.')) or ((board[0][0] == 'O') and (board[0][2] == 'O') and (board[0][1] == '.')):
                    coordinates_given_by_cpu = (0, 2)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'O') and (board[2][0] == 'O') and (board[1][0] == '.')) or ((board[1][1] == 'O') and (board[1][2] == 'O') and (board[1][0] == '.')):
                    coordinates_given_by_cpu = (1, 1)
                    return coordinates_given_by_cpu
                if ((board[1][0] == 'O') and (board[1][1] == 'O') and (board[1][2] == '.')) or ((board[0][2] == 'O') and (board[2][2] == 'O') and (board[1][2] == '.')):
                    coordinates_given_by_cpu = (1, 3)
                    return coordinates_given_by_cpu
                if ((board[0][1] == 'O') and (board[1][1] == 'O') and (board[2][1] == '.')) or ((board[2][0] == 'O') and (board[2][2] == 'O') and (board[2][1] == '.')):
                    coordinates_given_by_cpu = (2, 2)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'O') and (board[2][2] == 'O') and (board[1][1] == '.')) or ((board[2][0] == 'O') and (board[0][2] == 'O') and (board[1][1] == '.')) or ((board[1][0] == 'O') and (board[1][2] == 'O') and (board[1][1] == '.')) or ((board[0][1] == 'O') and (board[2][1] == 'O') and (board[1][1] == '.')):
                    coordinates_given_by_cpu = (1, 2)
                    return coordinates_given_by_cpu
                if ((board[2][0] == 'O') and (board[1][1] == 'O') and (board[0][2] == '.')) or ((board[0][0] == 'O') and (board[0][1] == 'O') and (board[0][2] == '.')) or ((board[1][2] == 'O') and (board[2][2] == 'O') and (board[0][2] == '.')):
                    coordinates_given_by_cpu = (0, 3)
                    return coordinates_given_by_cpu
                if ((board[1][1] == 'O') and (board[2][2] == 'O') and (board[0][0] == '.')) or ((board[1][0] == 'O') and (board[2][0] == 'O') and (board[0][0] == '.')) or ((board[0][1] == 'O') and (board[0][2] == 'O') and (board[0][0] == '.')):
                    coordinates_given_by_cpu = (0, 1)
                    return coordinates_given_by_cpu
                if ((board[0][2] == 'O') and (board[1][2] == 'O') and (board[2][2] == '.')) or ((board[2][0] == 'O') and (board[2][1] == 'O') and (board[2][2] == '.')) or ((board[0][0] == 'O') and (board[1][1] == 'O') and (board[2][2] == '.')):
                    coordinates_given_by_cpu = (2, 3)
                    return coordinates_given_by_cpu
                if ((board[0][0] == 'O') and (board[1][0] == 'O') and (board[2][0] == '.')) or ((board[1][1] == 'O') and (board[0][2] == 'O') and (board[2][0] == '.')) or ((board[2][1] == 'O') and (board[2][2] == 'O') and (board[2][0] == '.')):
                    coordinates_given_by_cpu = (2, 1)
                    return coordinates_given_by_cpu
                else:
                    for row in range(0, 3):
                        for col in range(0, 3):
                            if board[row][col] == '.':
                                coordinates_given_by_cpu = ((row), (col + 1))
                                return coordinates_given_by_cpu
        
    #elif difficulty_level == 1:
        #wszystko na randomie
        #pass
        



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
        print('WE HAVE A WINNER !\n'.center(width))
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
    print('\n\n\n\n████████╗██╗ ██████╗    ████████╗ █████╗  ██████╗    ████████╗ ██████╗ ███████╗')
    print('╚══██╔══╝██║██╔════╝    ╚══██╔══╝██╔══██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔════╝')
    print('   ██║   ██║██║            ██║   ███████║██║            ██║   ██║   ██║█████╗  ')
    print('   ██║   ██║██║            ██║   ██╔══██║██║            ██║   ██║   ██║██╔══╝  ')
    print('   ██║   ██║╚██████╗       ██║   ██║  ██║╚██████╗       ██║   ╚██████╔╝███████╗')
    print('   ╚═╝   ╚═╝ ╚═════╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝       ╚═╝    ╚═════╝ ╚══════╝\n\n')
    print('      1     2     3 \n'.center(width))
    print(('A     ' + str(board[0][0]) + '  ' +'|  ' + str(board[0][1]) + '  ' + '|  ' + str(board[0][2]) + '   ').center(width))
    print(('        ' + '----+-----+-----' + '    ').center(width))
    print(('B     ' + str(board[1][0]) + '  ' +'|  ' + str(board[1][1]) + '  ' + '|  ' + str(board[1][2]) + '   ').center(width))
    print(('        ' + '----+-----+-----' + '    ').center(width))
    print(('C     ' + str(board[2][0]) + '  ' +'|  ' + str(board[2][1]) + '  ' + '|  ' + str(board[2][2]) + '   ').center(width))
    print('\n')


# function print_result() stops main game loop, and when it occures prints one of two possible 
# results, win or a tie.
# If one of players win or its a tie, print_results returns True in order to stop main game loop
def print_result(player_mark, player_has_won, board_is_full):
    if player_has_won == True:
        print(('Player: " ' + str(player_mark) + ' "  IS THE WINNER !\n').center(width))  
        return True
    elif (player_has_won == False) and (board_is_full == True):
        print('LOOKS LIKE WE HAVE A TIE !\n'.center(width))
        print('--- nobody wins ---\n'.center(width))
        return True
    else:
        return False


# function tictactoe_game() uses previous functions together and runs a two 
# players game and provide turns, by changing a player sing from 'X' to 'O' in a loop. 
# It also checks, if user wants to quit by typing 'quit' instead of typing coordinates.
def tictactoe_game(board, player_mark, cpu_or_human_starts):
    player_switch = 1
    print_board(player_mark, board)
    game_is_over = False
    if cpu_or_human_starts == None: 
        while game_is_over == False:
            if (player_switch % 2 != 0):
                player_mark = 'X'
            elif (player_switch % 2 == 0):
                player_mark = 'O'

            coordinates = get_move(player_mark)

            if coordinates == ('quit'):
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n\nQuitting programm . . .\n\n--- BYE ! ---\n")
                sys.exit()
            mark(player_mark, board, coordinates)
            os.system('cls' if os.name == 'nt' else 'clear')
            print_board(player_mark, board)
            player_has_won = has_won(player_mark, board)
            board_is_full = is_full(player_mark, board)
            game_is_over = print_result(player_mark, player_has_won, board_is_full)
            player_switch += 1
    elif cpu_or_human_starts == 'HUMAN-AI':
        while game_is_over == False:
            if (player_switch % 2 != 0):
                player_mark = 'X'
                coordinates = get_move(player_mark)
            elif (player_switch % 2 == 0):
                player_mark = 'O'
                coordinates = get_ai_move(board, player_mark, cpu_or_human_starts, player_switch, difficulty_level)

            if coordinates == ('quit'):
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n\nQuitting programm . . .\n\n--- BYE ! ---\n")
                sys.exit()
            mark(player_mark, board, coordinates)
            os.system('cls' if os.name == 'nt' else 'clear')
            print_board(player_mark, board)
            player_has_won = has_won(player_mark, board)
            board_is_full = is_full(player_mark, board)
            game_is_over = print_result(player_mark, player_has_won, board_is_full)
            player_switch += 1
    elif cpu_or_human_starts == 'AI-HUMAN':
        while game_is_over == False:
            if (player_switch % 2 != 0):
                player_mark = 'X'
                coordinates = get_ai_move(board, player_mark, cpu_or_human_starts, player_switch, difficulty_level)
            elif (player_switch % 2 == 0):
                player_mark = 'O'
                coordinates = get_move(player_mark)

            if coordinates == ('quit'):
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n\nQuitting programm . . .\n\n--- BYE ! ---\n")
                sys.exit()
            mark(player_mark, board, coordinates)
            os.system('cls' if os.name == 'nt' else 'clear')
            print_board(player_mark, board)
            player_has_won = has_won(player_mark, board)
            board_is_full = is_full(player_mark, board)
            game_is_over = print_result(player_mark, player_has_won, board_is_full)
            player_switch += 1


def after_game():
    user_choice_after_game_valid = False
    while user_choice_after_game_valid == False:
        user_choice_after_game = str(input('1: Quick repeat\n2: Main menu\n0: Exit game\n'))
        if (user_choice_after_game == '1') or (user_choice_after_game == '0') or (user_choice_after_game == '2'):
            user_choice_after_game_valid = True
            return user_choice_after_game
        else:
            print('- - - WRONG INPUT - - -'.center(width))




# main game
#jesli aftergame() uzytkownik wybierze '2' funkcja zwraca 2 i nic sie nie dzieje, 
# petla wraca do menu glownego
main_game_loop = True
while main_game_loop == True:
    quick_repeat_choice = True
    user_choice_before_game = main_menu()
    if user_choice_before_game == '0':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\nQuitting programm . . .\n\n--- BYE ! ---\n")
        sys.exit()
    elif user_choice_before_game == '1':
        cpu_or_human_starts = None
        while quick_repeat_choice == True:
            board = init_board()
            player_mark = ('')
            os.system('cls' if os.name == 'nt' else 'clear')
            tictactoe_game(board, player_mark, cpu_or_human_starts)
            user_choice_after_game = after_game()
            if user_choice_after_game == '1':
                continue
            elif user_choice_after_game == '0':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n\nQuitting programm . . .\n\n--- BYE ! ---\n")
                sys.exit()
            quick_repeat_choice = False
            os.system('cls' if os.name == 'nt' else 'clear')
    elif user_choice_before_game == '2':
        user_choice_before_game_second_menu = second_menu()
        if user_choice_before_game_second_menu == '1':
            cpu_or_human_starts = 'HUMAN-AI'
        elif user_choice_before_game_second_menu == '2':
            cpu_or_human_starts = 'AI-HUMAN'
        difficulty_level = third_menu()
        while quick_repeat_choice == True:
            board = init_board()
            player_mark = ('')
            os.system('cls' if os.name == 'nt' else 'clear')
            tictactoe_game(board, player_mark, cpu_or_human_starts)
            user_choice_after_game = after_game()
            if user_choice_after_game == '1':
                continue
            elif user_choice_after_game == '0':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n\nQuitting programm . . .\n\n--- BYE ! ---\n")
                sys.exit()
            quick_repeat_choice = False
            os.system('cls' if os.name == 'nt' else 'clear')
        


