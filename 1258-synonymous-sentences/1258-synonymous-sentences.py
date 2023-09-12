class UnionFind():
    def __init__(self):
        self.parents = {}
    def find(self, u):
        self.parents.setdefault(u, u)
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        self.parents[v] = u

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        uf = UnionFind()
        
        for a,b in synonyms:
            uf.union(a, b)
            
        d = collections.defaultdict(set)
        for a, b in synonyms:
            root = uf.find(a)
            d[root] |= set([a, b])

        txt = text.split()
        res = []
        for t in txt:
            if t not in uf.parents:
                res.append([t])
            else:
                r = uf.find(t)
                res.append(list(d[r]))
        fin_res = [" ".join(sentence) for sentence in itertools.product(*res)]
        return sorted(fin_res)
        