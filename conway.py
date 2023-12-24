#import pygame

def print_board (board):
    [print(row) for row in board]
        
    
def initial_board(board):
    board[1][1]=1
    board[1][2]=1
    board[2][1]=1
    board[2][2]=1
    board[3][3]=1
    board[3][4]=1
    board[4][3]=1
    return board

def count_neighbours (board,x,y):
    sum=0   
    for i in range(0, 3):
        for j in range(0,3):
            if i==j==1:
                continue
            sum += board[x+i-1][y+j-1]                
    return sum
    

def padded_board (board,w,h): #add a perimeter of 0's to board to be able to run live_cell function
    new_board = [[0 for x in range(w+2)] for y in range(h+2)]
    for i in range(0, w):
        for j in range(0, h):
            new_board[i+1][j+1]=board[i][j]
    return new_board

                
def trim_edge(board, w, h):
    return [[board[x][y] for x in range(1, w+1)] for y in range(1, h+1)]


def matrix_to_board(board, w, h):
    #print(' _'*w)
    for j in range(0,h):
        for i in range(0,w):
            print('|{}'.format(board[j][i]), end = "")
        print('|')
        

def set_martix(board):
    """
    Reads the locations of life and set to the SparseMatrix
    """
    print("1. Enter positions of life with row,col format (e.g., 2,3).")
    print("2. Enter empty line to stop.")

    life=input()
    #coordList=[]
    while life:
        points=life.split(",")
        try:    
            x=int(points[0])
            y=int(points[1])
            board[x-1][y-1]=1
            #coord=[int(points[0]),int(points[1])]
            #coordList.append(coord)
        except ValueError:
            print("Ignored input:" + life+ ", row, col not valid numbers")
        except:
                print("Unexpected error:")
        print("added, keep entering or enter empty line to stop.")
        life=input()
    print("Thanks, finished entering live cells")
    return board
    
    
def main():
    
    n= int(input("What size grid would you like, between 5 and 10? (nxn) \n n = "))
    w,h= 5,5
    board = [[0 for x in range(w)] for y in range(h)] #define a board of wxh 0's
    set_martix(board)
    print("Initial board: ")
    #board=initial_board(board) #set board = initial board
    #print_board(board) #print initial board
    matrix_to_board(board, w, h)
    
    iterations = int(input("How many iterations would you like to do?" ))
    
    for a in range(1, iterations):
        padded_initial_board = padded_board(board,w,h)
        new = [[0 for x in range(w+2)] for y in range(h+2)] #define a board of (w+2)x(h+2) 0's
        
        for i in range(1, w+1):
            for j in range(1, h+1):
                n = count_neighbours(padded_initial_board,i,j) 
                val = padded_initial_board[i][j]
                if val == 1:
                    if (n == 2 or n == 3):
                        new[i][j] = 1
                if val == 0:
                    if n == 3:
                        new[i][j] = 1           
        
        board = trim_edge(new, w, h)
        print("Board {}:".format(a))
        matrix_to_board(board, w, h)
        #print_board(board)
        iterations += 1
        
if __name__ == "__main__":
    main()