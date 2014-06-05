#   |   |
# O |   |
#___|___|___
#   |   |
#   |   |
#___|___|___
#   |   |
#   |   |
#   |   |


# Print the board (board as shown above) wrote as a 3x3 list of lists where each element is a string that is either "O" or "X" or ' '
def print_board(board):
    i = 0
    print ('')
    for i in range(3):
        if i < 2:
            print ('   |   |   ')
            print (' ' + ' | '.join(board[i]))
            print ('___|___|___')
        else:
            print ('   |   |   ')
            print (' ' + ' | '.join(board[i]))
            print ('   |   |   ')
    return ''


# Intro to the game
def start_screen():
    print ("You are about to play O's and X's")
    player_1 = input("Who is going first? ")
    print ("Hi %s!" % (player_1))
    player_2 = input("Who is going second? ")
    print ("Hi %s!" % (player_2))
    answer = input("%s would you like to be O's or X's? " % (player_1)).lower()
    if answer == 'o' or answer == 0 or answer == "o's" or answer == "0's":
        player_1_piece = 'O'
        player_2_piece = 'X'
        print ("Excellent choice %s, you are O's. That means %s you are X's" % (player_1, player_2))
    elif answer == 'x' or answer == "x's":
        player_1_piece = 'X'
        player_2_piece = 'O'
        print ("Excellent choice %s, you are X's. That means %s you are O's" % (player_1, player_2))
    else:
        player_1_piece = 'O'
        player_2_piece = 'X'
        print ("If you won't say anything sensible I'll choose for you, %s you're now O's. %s you are X's and you shouldn't have any trouble beating %s!" % (player_1, player_2, player_1))
    print ("Every turn I will ask you to give me a row and column of where you want to go. The rows and columns range from 0 to 2.")
    print ("For example if you are X's say 11 the following board will appear on your first go.")
    print (print_board([[' ', ' ', ' '], [' ', 'X', ' '], [' ', ' ', ' ']]))
    return player_1, player_1_piece, player_2, player_2_piece

players = start_screen()
player_1 = players[0]
player_1_piece = players[1]
player_2 = players[2]
player_2_piece = players[3]


# Create an empty board

board = 3 * [3 * [' ']]
    



def is_this_a_valid_move(new_coord):
    # Is the length of the input correct?
    if len(new_coord) != 2:
        return False
    elif new_coord[0] in ['0', '1', '2'] and new_coord[1] in ['0', '1', '2']:
        row = int(new_coord[0])
        column = int(new_coord[1])
        # Have they chosen a valid co-ordinate?
        if row not in range(3) or column not in range(3):
            return False
        else:
            return True
    else:
        return False



def put_coords_onto_board(current_board, tile, new_coord):
    # What does the board have on it after a given go
    row = int(new_coord[0])
    column = int(new_coord[1])
    current_board[row][column] = tile
    return current_board




def has_somebody_won(current_board):
    # What does a given row or column look like
    row0 = current_board[0]
    row1 = current_board[1]
    row2 = current_board[2]
    column0 = [current_board[0][0]] + [current_board[1][0]] + [current_board[2][0]]
    column1 = [current_board[0][1]] + [current_board[1][1]] + [current_board[2][1]]
    column2 = [current_board[0][2]] + [current_board[1][2]] + [current_board[2][2]]
    # Have the got 3 in a row not diagonally
    if len(set(row0)) == 1 and row0[0] != ' ':
        return True
    elif len(set(row1)) == 1 and row1[0] != ' ':
        return True
    elif len(set(row2)) == 1 and row2[0] != ' ':
        return True
    elif len(set(column0)) == 1 and column0[0] != ' ':
        return True
    elif len(set(column1)) == 1 and column1[0] != ' ':
        return True
    elif len(set(column2)) == 1 and column2[0] != ' ':
        return True
    # Have they got 3 in a row diagonally?
    elif row0[0] == row1[1] == row2[2] and row0[0] != ' ':
        return True
    elif row0[2] == row1[1] == row2[0] and row2[0] != ' ':
        return True
    else:
        return False



def is_there_anyway_left_to_go(board):
    for row in board:
        for tile in row:
            if tile == ' ':
                return True
    return False



def would_you_like_to_play_again():
    answer = (input("Would you like to go again? y/n ")).lower()
    if answer == 'y':
        return game_play([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], 'player_2')
    elif answer == 'n':
        print ("OK, bye then...")
    else:
        print ("That's not a valid answer, try again...")
        return would_you_like_to_play_again()




def game_play(current_board, last_person_to_go): # Playing of the game
    # So we can keep up to date with whose turn it is
    if last_person_to_go == 'player_1':
        whose_go_is_it = 'player_2'
        name_of_whose_go_it_is = player_2
        tile_to_be_placed = player_2_piece
    else:
        whose_go_is_it = 'player_1'
        name_of_whose_go_it_is = player_1
        tile_to_be_placed = player_1_piece
    # How the board looks at the start of a given turn
    new_board = current_board
    answer = input("Where would you like to go %s? " % (name_of_whose_go_it_is))
    # Is the move allowed
    if is_this_a_valid_move(answer) == False:
        print ('That is not a valid move. Try again...')
        return game_play(new_board, last_person_to_go)
    else:
        # Where does someone want to go
        row = int(answer[0])
        column = int(answer[1])
        # Has someone gone there already
        if new_board[row][column] != ' ':
            print ("Someone has gone there already! Try again...")
            return game_play(current_board, last_person_to_go)
        else:
            # If the move is valid and they can go there
            new_board = put_coords_onto_board(new_board, tile_to_be_placed, answer)
            print(print_board(put_coords_onto_board(new_board, tile_to_be_placed, answer)))
            # Is that the end of the game?
            if has_somebody_won(new_board) == True:
                print ("You've won %s!" % (name_of_whose_go_it_is))
                return would_you_like_to_play_again()
            elif is_there_anyway_left_to_go(new_board) == False:
                print ("It's a draw!")
                return would_you_like_to_play_again()
            else:
                game_play(new_board, whose_go_is_it)
        

game_play([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], 'player_2')
            
        
        






