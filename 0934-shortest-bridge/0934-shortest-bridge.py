class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        def dfs(x, y):
            nonlocal q
            if grid[x][y] == 2:
                return
            grid[x][y] = 2
            q.append((x,y,0))
            for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                nx, ny = x+dx, y+dy
                if nx<0 or nx>=rows or ny<0 or ny>=cols:
                    continue
                if grid[nx][ny] == 1:
                    dfs(nx, ny)

        first_x, first_y = None, None
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    first_x, first_y = i , j
                    break
                    
        dfs(first_x, first_y)

        # print(seen, q)
        while q:
            x, y, d = q.popleft()
            for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                nx, ny = x+dx, y+dy
                if nx<0 or nx>=rows or ny<0 or ny>=cols:
                    continue
                if grid[nx][ny] == 2:
                    continue
                if grid[nx][ny] == 0:
                    grid[nx][ny] = 2
                    q.append((nx, ny, d+1))
                if grid[nx][ny] == 1:
                    return d