class Solution:
    area = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # DFS
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        def dfs(x, y):
            if visited[x][y]:
                return
            visited[x][y] = True
            self.area += 1
            for d in [[0,1], [0,-1], [1,0], [-1,0]]:
                next_x = x + d[0]
                next_y = y + d[1]
                if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]):
                    if not visited[next_x][next_y] and grid[next_x][next_y] == 1:
                        dfs(next_x, next_y)
        
        result = 0
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j] == 1:
                    self.area = 0
                    dfs(i, j)
                    result = max(result, self.area)
        return result
        
    
            