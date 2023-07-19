class Solution:
    def __init__(self):
        self.directions = [
            [0,1],
            [0,-1],
            [-1,0],
            [1,0]
        ]
        
    def dfs(self,grid,x,y):
        grid[x][y] = 'A'
        for i in range(4):
            next_x = x + self.directions[i][0]
            next_y = y + self.directions[i][1]
            if 0<=next_x<len(grid) and 0<=next_y<len(grid[0]):
                if grid[next_x][next_y] == "O":
                    self.dfs(grid,next_x,next_y)
                    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return None
        
        rows,cols = len(board), len(board[0])
        for i in range(rows):
            if board[i][0] == "O":
                self.dfs(board,i,0)
            if board[i][cols-1] == "O":
                self.dfs(board,i,cols-1)
                
        for j in range(cols):
            if board[0][j] == "O":
                self.dfs(board,0,j)
            if board[rows-1][j] == "O":
                self.dfs(board,rows-1,j)
        print(board)       
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"