from random import randrange
myboard=[[1,2,3],[4,5,6],[7,8,9]]
def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for row in board:
        num1,num2,num3=row
        print("""+--------+--------+--------+\n|        |        |        |""")
        print(
           "|   ",num1,"  |","  ",num2,"  |","  ",num3,"  |"
            )
        print("|        |        |        |")
    print("+--------+--------+--------+")

def enter_move(board):
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.
    global myboard
    pos=int(input("input an integer from 1 to 9:",))
    row=pos//3; col=pos%3-1
    if col==-1:
        col=2; row-=1
    if (row,col) not in make_list_of_free_fields(myboard):
        print("position occupied, reenter:")
        enter_move(myboard)
    else:
        myboard[row][col]="O"
    display_board(myboard)
    if victory_for(myboard, 'O')=='win':
        print("win")
        return
    if victory_for(myboard,'O')=='even':
        print("even")
        return
    
    draw_move(myboard)

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields=()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]!="O" and board[i][j]!="X":
                free_fields+=((i,j),)
    return free_fields

#print("free_fields:",make_list_of_free_fields(board))

def victory_for(board, sign):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    if board[0][0]==board[0][1]==board[0][2]==sign or \
        board[1][0]==board[1][1]==board[1][2]==sign or \
        board[2][0]==board[2][1]==board[2][2]==sign or \
        board[0][1]==board[1][1]==board[2][1]==sign or \
        board[0][2]==board[1][2]==board[2][2]==sign or \
        board[0][0]==board[1][0]==board[2][0]==sign or \
        board[0][0]==board[1][1]==board[2][2]==sign or \
        board[2][0]==board[1][1]==board[0][2]==sign:
            return "win"
    if len(make_list_of_free_fields(board))==0:
        return "even"
            

def draw_move(board):
    # The function draws the computer's move and updates the board.
    global myboard
    if myboard[1][1]!="X":
        myboard[1][1]="X"
    else:
        for i in range(10000):
            pos=randrange(1,10)
            row=pos//3; col=pos%3-1
            if col==-1:
                col=2; row-=1
            if (row,col) in make_list_of_free_fields(myboard):
                myboard[row][col]="X"
                break 
    display_board(myboard)
    if victory_for(myboard,'X')=='win':
        print("win")
        return
    if victory_for(myboard,'X')=='even':
        print("even")
        return
    enter_move(myboard)
            
draw_move(myboard)          
            
            
            
            
            
            
            
            