class Solution:                    
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        count = 0
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        
        def dfs(x,y):
            for d in dirs:
                nx = x + d[0]
                ny = y + d[1]
                if 0 <= nx < rows and 0 <= ny < cols:
                    if not visited[nx][ny] and grid[nx][ny] == "1":
                        visited[nx][ny] = True
                        dfs(nx, ny)
                        
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count
        