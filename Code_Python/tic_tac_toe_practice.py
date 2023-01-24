
def print_board(board):
    for row in board:
        print(row)

def check_status(player,board):
    for row in board:
        if row == [player,player,player]:
            return True

    for i in range(3):
        if board[0][0] == player and board[1][1] == player and board[2][2]:
            return True

        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True 

        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True    

    return False

def play_game(player,board):
     while True:
        print_board(board)
        row = int(input(f"Player {player}, enter the row between 0-2 "))
        col = int(input(f"Player {player}, enter the col between 0-2 "))
#        print("The row is ",row," and the col is ",col)

        if board[row][col] == ' ':
            board[row][col] = player

            if check_status(player,board):
                print(f"Player {player} wins !")
                break

            if player == 'X':
                player = 'O'
            else:
                player = 'X'
        

board = [[' ' for i in range(3)]
        for j in range(3)]

player = 'X'

play_game(player, board)