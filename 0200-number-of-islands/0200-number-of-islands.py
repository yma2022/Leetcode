class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            nonlocal seen
            if (x, y) in seen:
                return
            seen.add((x, y))
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = x+dx, y+dy
                if (nx, ny) in seen:
                    continue
                if nx<0 or nx>=len(grid) or ny<0 or ny>=len(grid[0]):
                    continue
                if grid[nx][ny] == '0':
                    continue
                dfs(nx, ny)
        count = 0
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                if (i, j) in seen:
                    continue
                dfs(i, j)
                count += 1
        return count
                
        