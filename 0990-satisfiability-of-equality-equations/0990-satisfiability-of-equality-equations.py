class UnionFind():
    def __init__(self):
        self.parents = {}
    def find(self, u):
        self.parents.setdefault(u, u)
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        self.parents[v] = u

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()
        
        for e in equations:
            if e[1] == '=':
                uf.union(e[0], e[3])
                
        for e in equations:
            if e[1] == '!':
                if uf.find(e[0]) == uf.find(e[3]):
                    return False
        return True
                    
        
        