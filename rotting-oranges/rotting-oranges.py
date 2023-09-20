class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        first_rot = None
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                grid[x][y] = -1
                for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = -1
                        q.append((nx, ny))
            res += 1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return res - 1 if res > 0 else res
        