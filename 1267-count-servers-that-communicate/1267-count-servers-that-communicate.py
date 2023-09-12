class UnionFind():
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.rank = [1] * size
    def find(self, u):
        if u == self.parents[u]:
            return u
        self.parents[u] = self.find(self.parents[u])
        return self.parents[u]
    def union(self, u, v):
        # print(u, v)
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return False
        if self.rank[u] > self.rank[v]:
            self.parents[v] = u
        elif self.rank[v] > self.rank[u]:
            self.parents[u] = v
        else:
            self.parents[v] = u
            self.rank[u] += 1
        return True

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ans = 0
        rows = len(grid)
        cols = len(grid[0])
        uf = UnionFind(rows * cols)
        for i in range(rows):
            curr = []
            for j in range(cols):
                if not curr and grid[i][j] == 1:
                    curr.append((i, j))
                elif curr and grid[i][j] == 1:
                    # print("i, j: ", i, j, curr[0])
                    uf.union(curr[0][0] * cols + curr[0][1], i * cols + j)
                    
 
        for j in range(cols):
            curr = []
            for i in range(rows):
                if not curr and grid[i][j] == 1:
                    curr.append((i, j))
                elif curr and grid[i][j] == 1:
                    uf.union(curr[0][0] * cols + curr[0][1], i * cols + j)

        for i, val in enumerate(uf.parents):
            if i == val and uf.rank[i] == 1:
                continue
            ans += 1
                                
        return ans
                
        