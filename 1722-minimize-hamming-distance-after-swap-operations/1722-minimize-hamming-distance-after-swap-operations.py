class UnionFind():
    def __init__(self, size):
        self.parents = [i for i in range(size)]
    def find(self, u):
        if u == self.parents[u]:
            return u
        self.parents[u] = self.find(self.parents[u])
        return self.parents[u]
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        self.parents[v] = u
        
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        uf = UnionFind(len(source))
        for x, y in allowedSwaps: 
            uf.union(x, y)
        m = defaultdict(set)  # key is the component, value is the set of indices in same component
        for i in range(len(source)):
            m[uf.find(i)].add(i)
        print(m.values())
        ans = 0
        for indices in m.values():
            A = [source[i] for i in indices]
            B = [target[i] for i in indices]
            print(A, B)
            ans += sum((Counter(A) - Counter(B)).values())
        
        return ans