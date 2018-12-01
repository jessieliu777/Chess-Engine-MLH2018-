import chess


def move(p, pr, board, finish, win):
    m = input(p + ', what is your move?')
    try:
        board.push_san(m)
        print(board)
    except:
        print(p + ' has done an illegal move')
        print(p + ', you have to lose because you broke the rules')
        finish = True
        win = pr
    if board.is_checkmate():
        print(pr + ' got checkmated!')
        finish = True
        win = p
    elif board.is_stalemate():
        print('stalemate')
        finish = True
    return finish, win

board = chess.Board()
win = None
print('welcome to text chess')
print('player 1 is white and player 2 is black')
p1 = input('enter name for player 1')
p2 = input('enter name for player 2')
print(board)
finish = False
while not finish:
    finish, win = move(p1, p2, board, finish, win)
    if not finish:
        finish, win = move(p2, p1, board, finish, win)
print('the winner is ' + str(win))
print('congratulations, ' + win + '!')
