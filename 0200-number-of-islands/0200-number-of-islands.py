class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            nonlocal seen
            for dx, dy in [[0,1], [0,-1], [1,0], [-1,0]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if grid[nx][ny] == "1" and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        dfs(nx, ny)
        seen = set()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in seen:
                    seen.add((i, j))
                    dfs(i, j)
                    count += 1
                    
        return count
                
                        
        