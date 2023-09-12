class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows = len(grid1)
        cols = len(grid1[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    grid2[i][j] = 2
        
        seen = set()
        def dfs(grid, x, y):
            if (x, y) in seen:
                return
            grid[x][y] = 0
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if grid[nx][ny] == 1 or grid[nx][ny] == 2:
                        dfs(grid, nx, ny)
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in seen and grid2[i][j] == 2:
                    dfs(grid2, i, j)
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in seen and grid2[i][j] == 1:
                    ans += 1
                    dfs(grid2, i, j)
        
        return ans
        