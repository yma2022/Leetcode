class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        rows = len(grid)
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        count = 0
        def dfs(x, y):
            if visited[x][y] or grid[x][y] == 1:
                return
            visited[x][y] = True
            for d in dirs:
                nx = x + d[0]
                ny = y + d[1]
                if 0 <= nx < rows and 0 <= ny < cols:
                    dfs(nx, ny)
                        
        for i in range(rows):
            if not visited[i][0] and grid[i][0] == 0:
                dfs(i, 0)
            if not visited[i][cols-1] and grid[i][cols-1] == 0:
                dfs(i, cols-1)        
        for j in range(cols):
            if not visited[0][j] and grid[0][j] == 0:
                dfs(0, j)
            if not visited[rows-1][j] and grid[rows-1][j] == 0:
                dfs(rows-1, j)
        print(visited)
        for i in range(1,rows):
            for j in range(1,cols):
                if not visited[i][j] and grid[i][j] == 0:
                    count += 1
                    dfs(i, j)
        return count
                    

                
        