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
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        uf = UnionFind(n+1)
        
        connections.sort(key = lambda x: x[2])
        ans = 0
        group = n
        for c in connections:
            if uf.union(c[0], c[1]):
                ans += c[2]
                group -= 1
        
        return ans if group == 1 else -1