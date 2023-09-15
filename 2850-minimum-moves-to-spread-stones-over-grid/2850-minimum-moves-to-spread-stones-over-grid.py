class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        dist = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])
        zeros, spare = [], []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    zeros.append((i, j))
                if grid[i][j] > 1:
                    spare.extend([(i, j)] * (grid[i][j] - 1))
                    
        return min((sum(map(dist, zeros, per))) for per in set(permutations(spare)))
    

#     class Solution:
#     def minimumMoves(self, grid: List[List[int]]) -> int:

#         dist = lambda x,y: abs(x[0]-y[0])+ abs(x[1]-y[1])  
#         zeros, spare = [], []

#         for i,j in product(range(3),range(3)):

#             stone = grid[i][j]
#             if stone == 0: zeros.append((i,j))               # <-- 1a)
#             if stone  > 1: spare.extend([(i,j)]*(stone-1))   # <-- 1b)

#         return min((sum(map(dist, zeros, per))) for per in   # <-- 2) and 3) 
#                                  set(permutations(spare)))
            
                            
        