class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        row,col = len(A),len(A[0])
        dirs = [(0,0),(-1,0),(0,-1),(1,0),(0,1)]
        island1 = collections.deque()
        
        def dfs(x, y):
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0<=nx<row and 0<=ny<col and A[nx][ny]==1:
                    A[nx][ny] = 2
                    island1.append([nx,ny])
                    dfs(nx,ny)
        
        for i in range(row):
            for j in range(col):
                if A[i][j] == 1:
                    first_x, first_y = i, j
                    break
        dfs(first_x,first_y)            
        #BFS Expand the island and count step
        step = 0
        while island1:
            for _ in range(len(island1)):
                x,y=island1.popleft()
                for dx,dy in dirs:
                    nx,ny = x+dx, y+dy
                    if 0<=nx<row and 0<=ny<col and A[nx][ny]!=2:
                        if A[nx][ny] == 0:
                            A[nx][ny]=2
                            island1.append([nx,ny])
                        elif A[nx][ny] == 1:
                            return step
            step+=1
        # return step