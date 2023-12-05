class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(x, y):
            if board[x][y] != 'O':
                return
            board[x][y] = '+'
            
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = x+dx, y+dy
                if nx<0 or nx>=len(board) or ny<0 or ny>=len(board[0]):
                    continue
                if board[nx][ny] != 'O':
                    continue
                dfs(nx,ny)
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][cols-1] == 'O':
                dfs(i, cols-1)
        for i in range(cols):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[rows-1][i] == 'O':
                dfs(rows-1, i)
                
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == '+':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'