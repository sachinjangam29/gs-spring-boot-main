
board = [['' for i in range(3)] for j in range(3)]

player = 'X'

def print_board():
    for row in board:
        print(row)


def check_win(player,board):
    for row in board:
        if row == [player,player,player]:
            return True

    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True

    #Check Diagnols
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return True

        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True

    return False       



def play_game(player,board):
    #print("The player "+player)
    while True:
        print_board()
        row = int(input(f"Player {player}, enter row (0-2):"))
        col = int(input(f"Player {player}, enter col (0-2):"))

        #print("Row is ",row)
        #print("Column is ",col)

        if board[row][col] == '':
            board[row][col] = player

            if check_win(player,board):
                print(f"Player {player} wins !")
                break

            if player == 'X':
                player = 'O'
            else:
                player = 'X'
        else:
            print("Invalid move, try again")

play_game(player,board)
