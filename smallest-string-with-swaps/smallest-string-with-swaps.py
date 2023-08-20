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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))
        
        for p in pairs:
            uf.union(p[0], p[1])
            
        d = collections.defaultdict(list)
        for i in range(len(s)):
            d[uf.find(i)].append(s[i])
        for key in d:
            d[key].sort()
            d[key].reverse()
        s_list = list(s)
        # print(d, s_list)
        for i in range(len(s)):
            s_list[i] = d[uf.find(i)].pop()
            
        return "".join(s_list)
               
        
        