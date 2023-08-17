class Solution:                    
#     def numIslands(self, grid: List[List[str]]) -> int:
#         rows = len(grid)
#         cols = len(grid[0])
#         visited = [[False for _ in range(cols)] for _ in range(rows)]
        
#         count = 0
#         dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        
#         def dfs(x,y):
#             for d in dirs:
#                 nx = x + d[0]
#                 ny = y + d[1]
#                 if 0 <= nx < rows and 0 <= ny < cols:
#                     if not visited[nx][ny] and grid[nx][ny] == "1":
#                         visited[nx][ny] = True
#                         dfs(nx, ny)
                        
#         for i in range(rows):
#             for j in range(cols):
#                 if not visited[i][j] and grid[i][j] == "1":
#                     dfs(i, j)
#                     count += 1
#         return count
        def numIslands(self, grid: List[List[str]]) -> int:
            if len(grid) == 0: return 0
            row = len(grid); col = len(grid[0])
            self.count = sum(grid[i][j]=='1' for i in range(row) for j in range(col))
            parent = [i for i in range(row*col)]

            def find(x):
                if parent[x]!= x:
                    return find(parent[x])
                return parent[x]

            def union(x,y):
                xroot, yroot = find(x),find(y)
                if xroot == yroot: return 
                parent[xroot] = yroot
                self.count -= 1



            for i in range(row):
                for j in range(col):
                    if grid[i][j] == '0':
                        continue
                    index = i*col + j
                    if j < col-1 and grid[i][j+1] == '1':
                        union(index, index+1)
                    if i < row-1 and grid[i+1][j] == '1':
                        union(index, index+col)
            return self.count