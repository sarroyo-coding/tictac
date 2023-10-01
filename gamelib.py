import re

def draw_board (board):
    for row in board:
        print("")
        for space in row:
            if space == 0:
                print(" - ", end = '')
            elif space == -1:
                print(" X ", end = '')
            elif space == 1:
                print(" O ", end = '')
    return ""


def turn_prompt():
    valid_input = re.compile('[0-2]')

    loc_x = ""
    while valid_input.match(loc_x) is None:
        loc_x = input("choose a row 0-2: ")
        if valid_input.match(loc_x) is None:
            print("try again")

    loc_y = ""
    while valid_input.match(loc_y) is None:
        loc_y = input("choose a column 0-2: ")
        if valid_input.match(loc_y) is None:
            print("try again")
    
    return int(loc_x), int(loc_y)

def check_move(board, x, y):
    # if the x y location of the board is blank then true 
    return board[x][y] == 0


def check_win(board):
    # check for row wins
    for row in board:
        sum = 0
        for i in row:
            sum+=i
        if sum == 3 or sum == -3:
            return True  
    # check for col wins 
    for i in range (0,3):
        sum = 0
        for row in board:
            sum += row[i]
        if sum == 3 or sum == -3:
            return True
                
    if abs(board[0][0] + board[1][1] + board[2][2]) == 3:
        return True
    
    if abs(board[0][2] + board[1][1] + board[2][0]) == 3:
        return True
    
    return False

def is_stalemate(board):
  for row in board: 
    for i in row:
      if i == 0:
        return False
  return True


def num_to_name(whos_turn):
    if whos_turn == -1:
        return "Player 1"
    return "Player 2"