class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            nonlocal seen
            if (x,y) in seen:
                return
            seen.add((x,y))
            
            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                nx, ny = x+dx, y+dy
                if nx<0 or nx>=len(grid) or ny<0 or ny>=len(grid[0]):
                    continue
                if (nx, ny) in seen or grid[nx][ny] !="1":
                    continue
                dfs(nx, ny)
                
                
        seen = set()
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in seen:
                    dfs(i, j)
                    count += 1
                    
        return count
        