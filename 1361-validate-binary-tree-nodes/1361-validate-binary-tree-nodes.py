class UnionFind():
    def __init__(self, size):
        self.parents = [i for i in range(size)]
    def find(self, u):
        if self.parents[u] == u:
            return u
        self.parents[u] = self.find(self.parents[u])
        return self.parents[u]
    
    def union(self, u, v):
        u_parent = self.find(u)
        v_parent = self.find(v)
        if u_parent != v_parent:
            self.parents[v] = u_parent

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        uf = UnionFind(n)
        components = n
        for i in range(n):
            lc = leftChild[i]
            rc = rightChild[i]
            for child in [lc, rc]:
                if child == -1:
                    continue
                if uf.find(child) == uf.find(i) or uf.find(child) != child:
                    return False
                uf.union(i, child)
                components -= 1
        return components == 1
            
        