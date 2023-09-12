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
        if self.rank[u] > self.rank[v]:
            self.parents[v] = u
        elif self.rank[v] > self.rank[u]:
            self.parents[u] = v
        else:
            self.parents[v] = u
            self.rank[u] += 1

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind(26)
        d = collections.defaultdict(list)
        for i in range(len(s1)):
            if uf.find(ord(s1[i]) - ord('a')) != uf.find(ord(s2[i]) - ord('a')):
                uf.union(ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a'))
        for i in range(len(uf.parents)):
            d[uf.parents[i]].append(chr(i + ord('a')))
            
        ans = "" 
        for c in baseStr:
            if uf.find((ord(c)) - ord('a')) in d:
                d[uf.find((ord(c)) - ord('a'))].sort()
                ans += d[uf.find((ord(c)) - ord('a'))][0]
            else:
                ans += c
                
        return ans
        