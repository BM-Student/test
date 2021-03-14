import random
print('The positions are zero indexed')

def game_loop():
    board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

    # Computer Move
    def computer_move(b):
        available_positions = []
        for i in range(len(b)):
            for j in range(len(b[i])):
                if b[i][j] != 'X':
                    available_positions.append([i, j])
        spot = random.choice(available_positions)
        board[spot[0]][spot[1]] = 'O'
        check_win(b)
        print_board(b)


    # Player Move
    def player_move(b):
        ans = input('Where do you place your mark(X)? Enter as row,column')
        if len(ans) == 3:
            if board[int(ans[0])][int(ans[2])] != 'O' and board[int(ans[0])][int(ans[2])] != 'X':
                board[int(ans[0])][int(ans[2])] = 'X'
                check_win(b)
                computer_move(b)
            else:
                print('This spot is already assigned. Pick again.')
                player_move(b)
        else:
            print('Invalid input. Pick again.')
            player_move(b)


    # Board
    def print_board(b):
        print('The board\'s current state is...')
        for i in b:
            print(i)
        player_move(b)

    # Win Conditions
    def check_win(b):
        # Player wins
        if b[0] == ['X', 'X', 'X'] or b[1] == ['X', 'X', 'X'] or b[2] == ['X', 'X', 'X'] or \
                (b[0][0] == 'X' and b[1][1] == 'X' and b[2][2] == 'X'):
            print('The player won!! \(^_^)/')
            game_loop()
        elif b[0] == ['O', 'O', 'O'] or b[1] == ['O', 'O', 'O'] or b[2] == ['O', 'O', 'O'] or \
                (b[0][0] == 'O' and b[1][1] == 'O' and b[2][2] == 'O'):
            print('The computer won (-_-)')
            game_loop()

        column_0 = []
        column_1 = []
        column_2 = []

        for i in range(len(b)):
            column_0.append(b[i][0])
        for i in range(len(b)):
            column_1.append(b[i][1])
        for i in range(len(b)):
            column_2.append(b[i][2])

        if column_0 == ['X', 'X', 'X'] or column_1 == ['X', 'X', 'X'] or column_2 == ['X', 'X', 'X']:
            print('The player won!! \(^_^)/')
            game_loop()
        elif column_0 == ['O', 'O', 'O'] or column_1 == ['O', 'O', 'O'] or column_2 == ['O', 'O', 'O']:
            print('The computer won (-_-)')
            game_loop()


    print_board(board)

game_loop()