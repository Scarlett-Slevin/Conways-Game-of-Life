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

def trim_edge(board,w,h):
    return [[board[x][y] for x in range(1,w+1)] for y in range(1,h+1)]

                
def main():
    w,h=5,5
    board = [[0 for x in range(w)] for y in range(h)] #define a board of wxh 0's
    board=initial_board(board) #set board = initial board
    print("Initial board: ")
    print_board(board) #print initial board
    new = [[0 for x in range(w+2)] for y in range(h+2)] #define a board of (w+2)x(h+2) 0's
    padded_initial_board = padded_board(initial_board(board),w,h)
    for i in range(1, w+1):
        for j in range(1, h+1):
            n = count_neighbours(padded_initial_board,i,j) 
            if padded_initial_board[i][j]==1:
                if (n == 2 or n == 3):
                    new[i][j] = 1
            if padded_initial_board[i][j]==0:
                if n == 3:
                    new[i][j] = 1

    #print("New board: ")
    #print_board(new)
    print("Final board: ")
    print_board(trim_edge(new,w,h))


        
if __name__ == "__main__":
    main()