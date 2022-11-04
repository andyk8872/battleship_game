'''Import python libraries'''
from random import randint
import os
# import pyfiglet
from battleship_art import LOGO, WIN, LOSE, DRAW


COMP_UNSEEN_GRID = [['.']*5 for x in range(5)]
COMP_SEEN_GRID = [['.']*5 for x in range(5)]
PLAYER_SEEN_GRID = [['.']*5 for x in range(5)]
NO_OF_SHIPS = 0
COMP_SCORE = 0


def clear():
    """
    A function to clear the screen
    """
    os.system('clear')


def introduction():
    """
    Description of the game and instructions
    """
    print(LOGO)
    print("*-----Intstructions-----*")
    print("It's you againest the computer.")
    print("Who can sink the others ships.")
    print("First choose the number of ships for the battle.\n")
    print('Welcome to Battleship\n')


def battle_zone(board):
    """
    Create function to create game area
    """
    print('    C o l u m n')
    print('    1   2   3   4   5')
    print('   * * * * * * * * *')
    row_legend = 1
    row_text = [' ', 'R', 'O', 'W', ' ']
    for x_row, row in zip(row_text, board):
        print(x_row, row_legend,  " | ".join(row))
        row_legend += 1


# def create__ships(board, NO_OF_SHIPS):
#     """
#     Function that creates the ships and
#     places them in the game area, but not in the
#     same location
#     """
#     pass


def find_ship_location():
    """
    A function to locate the ships
    """
    while True:
        row = input('\nPlease enter a ship row 1 - 5 ')    
        if validate_location_data(row):            
            break
    while True:
        column = input('Please enter a ship column 1 - 5 ')     
        if validate_location_data(column):            
            clear()
            print(LOGO)
            break

    return int(row) - 1, int(column) - 1


def validate_location_data(input):
    """
    A function to validate player location input
    """
    try:    
        input = int(input)
        if input not in range(1, 6):
            raise ValueError(f"A number: 1 - 5 required, you provided {input}")
    except ValueError as e_e:
        print(f"Invalid data: {e_e}, please try again.\n")
        return False      
    return True


def get_player_location():
    """
    A function to locate players ships
    """
    player_row = randint(0, 4)
    player_column = randint(0, 4)
    return player_row, player_column


def comp_turn():
    """
    A function to for the computer to choose
    """
    global COMP_SCORE       
    player_row, player_column = get_player_location()  
    if PLAYER_SEEN_GRID[player_row][player_column] =='X':          
        PLAYER_SEEN_GRID[player_row][player_column] = 'H'    
        COMP_SCORE += 1
    else:      
        PLAYER_SEEN_GRID[player_row][player_column] = 'M'


def play_again():
    """
    A function to enable a replay
    """
    global COMP_SEEN_GRID, COMP_UNSEEN_GRID, PLAYER_SEEN_GRID  
    while True:
        replay = input("Type 'y' to play again\nor 'Q' to leave: ").upper()
        if replay == 'Q':
            clear()
            print('Goodbye')
            break
        elif replay == 'Y':
            COMP_UNSEEN_GRID = [['.']*5 for x in range(5)]
            COMP_SEEN_GRID = [['.']*5 for x in range(5)]
            PLAYER_SEEN_GRID = [['.']*5 for x in range(5)]
            clear()
            setup()
        else:
            print("Incorrect entry, type 'Y/y' to play again or 'Q/q' to Quit")        
            continue


def get_no_of_ships():
    """
    A function to choose the number of ships
    """
    while True:
        no_of_ships = input("Enter the number here of ships \
(between 10 an 15) :\nExample: 11\n")
        if validate_ship_data(no_of_ships):
            print("Data is valid")
            break
    return no_of_ships


def validate_ship_data(no_of_ships):
    """
    A function to validate player input
    """
    try:
        no_of_ships = int(no_of_ships)
        if no_of_ships not in range(11, 15):
            raise ValueError(f"A number between 10 and 15 required, \
you provided {no_of_ships}")
    except ValueError as e_e:
        print(f"Invalid data: {e_e}, please try again.\n")
        return False
    return True


def create_ships(board, NO_OF_SHIPS):
    """
    Function that creates the ships and
    places them in the game area, but not in the
    same location
    """
    for ship in range(NO_OF_SHIPS):       
        ship_row, ship_col = randint(0, 4), randint(0, 4)
        while board[ship_row][ship_col] == 'X':
            ship_row, ship_col = randint(0, 4), randint(0, 4)
        board[ship_row][ship_col] = 'X'
    return


def main(player, computer):
    """
    The main game function
    """
    global COMP_SCORE
    COMP_SCORE = 0
    turns = 5
    player_score = 0
    while turns > 0:      
        print("\nComputer Arena\n")
        battle_zone(COMP_SEEN_GRID)      
        battle_zone(COMP_UNSEEN_GRID)
        print("\nPlayer Arena\n")
        battle_zone(PLAYER_SEEN_GRID)
        comp_turn()    
        row, column = find_ship_location()
        if COMP_SEEN_GRID[row][column] == 'o' or \
            COMP_SEEN_GRID[row][column] == 'X':
            print(' You already guessed that\n')        
        elif COMP_UNSEEN_GRID[row][column] =='X':          
            print('Congratulations you have hit a battleship\n')          
            COMP_SEEN_GRID[row][column] = 'X'          
            turns -= 1
            player_score += 1
            print(f"PlayerScore: {player_score}")
            print(f"Computer Score: {COMP_SCORE}")          
        elif COMP_SEEN_GRID[row][column] == '.':
            print('Sorry,You missed\n')
            COMP_SEEN_GRID[row][column] =  'o'
            turns -= 1
            print(f"Player Score: {player_score}")
            print(f"Comp Score: {COMP_SCORE}")
        print("You have " + str(turns) + " turns remaining\n")
        if turns == 0:
            print('Game Over ')
            if player_score == COMP_SCORE:            
                print(DRAW)
                print(f"Player Score: {player_score}")
                print(f"Computer Score: {COMP_SCORE}\n")
                play_again()
            elif player_score > COMP_SCORE:
                print(WIN)
                print(f"Player Score: {player_score}")
                print(f"Computer Score: {COMP_SCORE}\n")
                play_again()
            elif player_score < COMP_SCORE:            
                print(LOSE)
                print(f"PlayerScore: {player_score}")
                print(f"Computer Score: {COMP_SCORE}\n")
                play_again()
            break


def setup():
    """
    A function to set game parameters
    """
    clear()
    introduction()
    ships = get_no_of_ships()
    NO_OF_SHIPS = int(ships)
    computer = create_ships(COMP_UNSEEN_GRID, NO_OF_SHIPS)
    player = create_ships(PLAYER_SEEN_GRID, NO_OF_SHIPS)
    main(player, computer) 


setup()