class Solution:
    def __init__(self):
        self.directions = [
            [0,1],
            [1,0],
            [-1,0],
            [0,-1]
        ]
    def dfs(self,grid, visited, x, y):
        for i in range(4):
            next_x = x + self.directions[i][0]
            next_y = y + self.directions[i][1]
            
            if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]):
                if not visited[next_x][next_y] and grid[next_x][next_y] == '1':
                    visited[next_x][next_y] = True
                    self.dfs(grid, visited, next_x, next_y)
                    
    def numIslands(self, grid: List[List[str]]) -> int:
        cols = len(grid)
        rows = len(grid[0])
        visited = [[False for _ in range(rows)] for _ in range(cols)]
        res = 0
        # print(visited, grid)
        for i in range(cols):
            for j in range(rows):
                if not visited[i][j] and grid[i][j] == '1':
                    visited[i][j] = True
                    res += 1
                    self.dfs(grid, visited, i, j)
        return res
        