def print_board (board):
    [print(row) for row in board]
        
    
def init_board(board):
    board[1][1]=1
    board[1][2]=1
    board[2][1]=1
    board[2][2]=1
    board[3][3]=1
    board[3][4]=1
    board[4][3]=1
    return board

def live_cell (board):
    sum=0
    x=1
    y=1
    #for x in range(w):
        #for y in range(h):   
    for i in range(0, 3):
        for j in range(0,3):
            sum += board[x+i-1][y+j-1]
                
    return sum
                
                
def main():
    w,h=5,5
    board = [[0 for x in range(w)] for y in range(h)]
    print_board(init_board(board))
    print(live_cell(init_board(board)))
        
if __name__ == "__main__":
    main()