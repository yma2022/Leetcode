class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        M = len(grid)
        N = len(grid[0])

        #visited set, to not visit the same nodes again
        v= set()

        dirs=[[0,1],[1,0]]

        path = set()
        
        v.add((0,0))
        path.add((0,0))
        
        def dfs(x,y):
            
            if x == M -1 and y == N -1:
                return True
            
            for d in dirs:
                nx = x + d[0]
                ny = y + d[1]
                
                if nx < M and ny < N and (nx,ny) not in v and grid[nx][ny] == 1:
                    v.add((nx,ny))
                    path.add((nx,ny))
                    if dfs(nx,ny):
                        return True
                    path.remove((nx,ny))
            return False

        # 1 do a dfs from (0,0) to (M-1,N-1) 
        res =  dfs(0,0)
        
        # if there is no path the it's already disconnectd, return True
        if not res:
            return True
        
        # remove the first and last node from the path
        if (0,0) in path:
            path.remove((0,0))
        if (M-1,N-1) in path:
            path.remove((M-1,N-1))
        
        # 2 remove the path from the grid
        for p in path:
            grid[p[0]][p[1]] = 0
        
        #reset the visited set
        v= set()
        v.add((0,0))

        # 3 try again DFS, if it's not connected, return True
        return not dfs(0,0)