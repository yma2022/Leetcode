class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        o_set = set()
        
        rows = len(board)
        cols = len(board[0])
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    o_set.add((i, j))
                    board[i][j] = "X"
                    
        def dfs(x, y):
            nonlocal seen
            if (x, y) in seen:
                return
            seen.add((x, y))
            board[x][y] = "O"
            for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
                nx, ny = x+dx, y+dy
                if nx<0 or nx>=rows or ny<0 or ny>=cols:
                    continue
                if (nx, ny) not in o_set or (nx, ny) in seen:
                    continue
                dfs(nx, ny)
        seen = set()
        
        for i in range(rows):
            if (i ,0) in o_set:
                dfs(i, 0)
            if (i, cols-1) in o_set:
                dfs(i, cols-1)
        for i in range(cols):
            if (0, i) in o_set:
                dfs(0, i)
            if (rows-1, i) in o_set:
                dfs(rows-1, i)