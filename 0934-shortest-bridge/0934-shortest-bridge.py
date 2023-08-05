class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        rows, cols = len(A), len(A[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        island1 = deque()
        def dfs(x, y):
            if A[x][y] == 0:
                return
            A[x][y] = 2
            island1.append([x, y])
            for d in dirs:
                nx = x + d[0]
                ny = y + d[1]
                if 0 <= nx < rows and 0 <= ny < cols:
                    if A[nx][ny] == 1:                        
                        dfs(nx, ny)
        first_x, first_y = 0, 0            
        for i in range(rows):
            for j in range(cols):
                if A[i][j] == 1:
                    first_x, first_y = i, j
                    break
        dfs(first_x, first_y)
        length = 0
        print(island1)
        while island1:
            for _ in range(len(island1)):
                x,y=island1.popleft()
                for d in dirs:
                    nx,ny = x+d[0], y+d[1]
                    if 0<=nx<rows and 0<=ny<cols and A[nx][ny]!=2:
                        if A[nx][ny] == 0:
                            A[nx][ny]=2
                            island1.append([nx,ny])
                        elif A[nx][ny] == 1:
                            return length
            length += 1
        return length          