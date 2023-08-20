class UnionFind:
    def __init__(self, size):
        self.parent= [i for i in range(size)]
        self.rank = [1] * size
    def find(self, u):
        if u == self.parent[u]:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            if self.rank[u] > self.rank[v]:
                self.parent[v] = u
            elif self.rank[v] > self.rank[u]:
                self.parent[u] = v
            else:
                self.parent[v] = u
                self.rank[u] += 1
                
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        group = n
        for e in edges:
            if uf.find(e[0]) != uf.find(e[1]):
                uf.union(e[0], e[1])
                group -= 1
        return group
        