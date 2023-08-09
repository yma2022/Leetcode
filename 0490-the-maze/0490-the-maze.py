class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        stop = set()
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(x, y):
            if (x, y) in stop:
                return False
            stop.add((x,y))
            if [x,y] == destination:
                return True
            for dx, dy in dirs:
                nx, ny = x, y
                while 0 <= nx + dx < len(maze) and 0 <= ny + dy < len(maze[0]) and maze[nx+dx][ny+dy] != 1:
                    nx += dx
                    ny += dy
                if dfs(nx, ny):
                    return True
            return False
        return dfs(start[0], start[1])

    
    # def hasPath(self, maze, start, destination):
    #     m, n, stopped = len(maze), len(maze[0]), set()
    #     def dfs(x, y):
    #         if (x, y) in stopped: 
    #             return False
    #         stopped.add((x, y))
    #         if [x, y] == destination:
    #             return True
    #         for i, j in (-1, 0) , (1, 0), (0, -1), (0, 1):
    #             newX, newY = x, y
    #             while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
    #                 newX += i
    #                 newY += j
    #             if dfs(newX, newY):
    #                 return True
    #         return False
    #     return dfs(*start)
                
        