class Solution:    

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        self.parent = [i for i in range(n+1)]
        
        def find(u):
            if u == self.parent[u]:
                return u
            self.parent[u] = find(self.parent[u])
            return self.parent[u]
            
        def join(u, v):
            u = find(u)
            v = find(v)
            if u == v:
                return
            self.parent[v] = u
            pass
            
            
        for i in range(len(edges)):
            if find(edges[i][0]) == find(edges[i][1]) :
                return edges[i]
            else :
                join(edges[i][0], edges[i][1])
        return []
        