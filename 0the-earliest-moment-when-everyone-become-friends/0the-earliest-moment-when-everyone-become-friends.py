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
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key = lambda x: x[0])
        group = n
        uf = UnionFind(n)
        for l in logs:
            if uf.find(l[1]) != uf.find(l[2]):
                group -= 1
                uf.union(l[1], l[2])
                if group == 1:
                    return l[0]
        return -1
        