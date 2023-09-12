# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass
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
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
        uf = UnionFind(n)
        ans = n
        for i in range(n):
            for j in range(i+1, n):
                if categoryHandler.haveSameCategory(i, j) and uf.find(i) != uf.find(j):
                    uf.union(i, j)
                    ans -= 1
        return ans
        