
import random

def clear_screen( numlines = 100 ) :
	print ( '\n' * numlines )

def create_board() :
    board = [ [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '] ]
    return board

def random_ints( board ) :
    raw = random.randint(0,2)
    column = random.randint(0,3)
    while board[raw][column] != ' ' :
            raw = random.randint(0,2)
            column = random.randint(0,3)
    return raw,column

def fill_board() :
    board = create_board()
    i = 0
    while( i < 6) :
        raw,column = random_ints(board)
        board[raw][column] = chr(ord('A')+i)
        raw,column = random_ints(board)
        board[raw][column] = chr(ord('A')+i)
        i += 1
    return board

def print_board(board):
    print( '\n|'+' '+board[0][0]+' '+'|'+' '+board[0][1]+' '+'|'+' '+board[0][2]+' '+'|'+' '+board[0][3]+' '+'|')
    print( '|---|---|---|---|')
    print( '|'+' '+board[1][0]+' '+'|'+' '+board[1][1]+' '+'|'+' '+board[1][2]+' '+'|'+' '+board[1][3]+' '+'|')
    print( '|---|---|---|---|')
    print( '|'+' '+board[2][0]+' '+'|'+' '+board[2][1]+' '+'|'+' '+board[2][2]+' '+'|'+' '+board[2][3]+' '+'|')
    print( '|---|---|---|---|\n')

def spaces(board):
    s = 0
    for i in range(3):
        for k in range(4):
            if board[i][k]==' ':
                s = s+1
    return s

def ready():
    a = input('are you ready : ')
    while a!='ok':
        print('say ok')
        a = input('are you ready : ')

def take_input(spaces_board):
    i,k = tuple(map(int,input('give position as a tuple e.g. 2,2 : ').split(',')))
    m,n = tuple(map(int,input('give position as a tuple e.g. 2,2 : ').split(',')))
    while k<0 or i<0 or i>2 or k>3 or spaces_board[i][k]!=' ':
            i,k = tuple(map(int,input('give first position again as a tuple e.g. 2,2 : ').split(',')))
    while m<0 or n<0 or m>2 or n>3 or spaces_board[m][n]!=' ' or (i==m and k==n):
            m,n = tuple(map(int,input('give first position again as a tuple e.g. 2,2 : ').split(',')))
    return i,k,m,n

def memo(full_board,spaces_board):
    while ( True ) :
        i,k,m,n = take_input(spaces_board)
        if full_board[i][k]==full_board[m][n]:
            spaces_board[i][k] = full_board[i][k]
            spaces_board[m][n] = full_board[m][n]
            if spaces(spaces_board)>2:
                print_board(spaces_board)
                continue
            else:
                print_board(full_board)
                print('you win!\n')
                break
        else:
            error_board = create_board()
            error_board[i][k] = full_board[i][k]
            error_board[m][n] = full_board[m][n]
            print_board(error_board)
            del error_board
            ready()

def main():
    full_board = fill_board()
    spaces_board = create_board()
    print_board(full_board)
    ready()
    clear_screen()
    print_board(spaces_board)
    memo(full_board,spaces_board)

main()
