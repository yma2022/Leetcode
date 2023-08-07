class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n, m = len(grid), len(grid[0])
        cnt = 0
        g = [[0 for _ in range(3*n)] for _ in range(3*m)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '/':
                    g[i * 3][j * 3 + 2] = 1
                    g[i * 3 + 1][j * 3 + 1] = 1
                    g[i * 3 + 2][j * 3] = 1
                elif grid[i][j] == '\\':
                    g[i * 3][j * 3] = 1
                    g[i * 3 + 1][j * 3 + 1] = 1
                    g[i * 3 + 2][j * 3 + 2] = 1
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        # print(g)
        def dfs(x, y):
            visited[x][y] = True
            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < len(g) and 0 <= ny < len(g[0]):
                    if not visited[nx][ny] and g[nx][ny] == 0:
                        dfs(nx, ny)
        res = 0
        visited = [[False for _ in range(len(g[0]))] for _ in range(len(g))]
        for i in range(len(g)):
            for j in range(len(g[0])):
                if not visited[i][j] and g[i][j] == 0:
                    res += 1
                    dfs(i, j)
                    
        return res