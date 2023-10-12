class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        q = deque()
        cols = len(mat[0])
        rows = len(mat)
        ans = [[0 for _ in range(cols)] for _ in range(rows)]
        seen = set()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    seen.add((i, j))
        
        while q:
            x, y, step = q.popleft()

            for dx, dy in [[0,1], [0,-1], [1,0], [-1,0]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in seen:
                    ans[nx][ny] = step + 1
                    q.append((nx, ny, step + 1))
                    seen.add((nx, ny))
        return ans
        