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
    def removeStones(self, stones: List[List[int]]) -> int:
        k = 10001
        n = len(stones)
        marked = collections.defaultdict()
        uf = UnionFind(2 * k + 1)
        ans = 0
        for i in range(n):
            if uf.find(stones[i][0]) not in marked:
                ans += 1
            if uf.find(stones[i][1] + k) not in marked:
                ans += 1
            marked[stones[i][0]] = marked.get(stones[i][0], 0) + 1
            marked[stones[i][1] + k] = marked.get(stones[i][1] + k, 0) + 1
            
        for i in range(n):
            x = stones[i][0]
            y = stones[i][1] + k
            
            ans -= uf.union(x, y)
        
        return n - ans     
                
        