class Solution:
    def __init__(self):
        self.enclaves = True
        self.count = 0
        self.directions = [
            [0,1],
            [0,-1],
            [-1,0],
            [1,0]
        ]
        
    def dfs(self,grid,visited,x,y):
        for i in range(4):
            next_x = x + self.directions[i][0]
            next_y = y + self.directions[i][1]
            
            if 0<=next_x<len(grid) and 0<=next_y<len(grid[0]):
                if not visited[next_x][next_y] and grid[next_x][next_y] == 1:
                    visited[next_x][next_y] = True
                    if next_x in [0, len(grid)-1] or next_y in [0, len(grid[0])-1]:
                        self.enclaves = False
                    self.count += 1
                    self.dfs(grid,visited,next_x,next_y)
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid:
            return None
        
        cols,rows = len(grid), len(grid[0])
        visited = [[False for row in range(rows)]for col in range(cols)]
        res = 0
        for i in range(cols):
            for j in range(rows):
                if not visited[i][j] and grid[i][j] == 1:
                    visited[i][j] = True
                    if i in [0, len(grid)-1] or j in [0, len(grid[0])-1]:
                        self.enclaves = False
                    self.count = 1
                    self.dfs(grid,visited,i,j)
                    if self.enclaves:
                        res += self.count
                    self.enclaves = True
        return res
                
        