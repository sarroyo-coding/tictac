import gamelib

init_board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]


def play(whos_turn, board):
    won = False

    while won is False:
        print("{}'s turn:".format(gamelib.num_to_name(whos_turn)))
        print(gamelib.draw_board(board))

        # try do move
        x, y = gamelib.turn_prompt()
        while not gamelib.check_move(board, x, y):
            print('try again')
            print(gamelib.draw_board(board))
            x, y = gamelib.turn_prompt()

        # do move
        board[x][y] = whos_turn

        # check win
        if gamelib.check_win(board):
            won = True
        elif gamelib.is_stalemate(board):
            for x in range(0,3):
                for y in range(0,3):
                    board[x][y] = 0
            print("Stalemate! Restarting")
        else:
            # switch turn
            whos_turn = whos_turn * -1


    gamelib.draw_board(board)
    print("{} won!!!".format(gamelib.num_to_name(whos_turn)))


play(-1, init_board)