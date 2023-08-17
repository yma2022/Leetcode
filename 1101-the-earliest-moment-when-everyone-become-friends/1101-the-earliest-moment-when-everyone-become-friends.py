class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        def find(u):
            if u == parent[u]:
                return u
            parent[u] = find(parent[u])
            return parent[u]
        
        def join(u, v):
            u = find(u)
            v = find(v)
            if u == v:
                return
            if rank[u] > rank[v]:
                parent[v] = u
            elif rank[u] < rank[v]:
                parent[u] = v
            else:
                parent[v] = u
                rank[u] += 1
                
        parent = [i for i in range(n)]
        rank = [0 for _ in range(n)]
        logs.sort(key = lambda x: x[0])
        group = n
        for l in logs:
            if find(l[1]) != find(l[2]):
                group -= 1
                join(l[1], l[2])
                if group == 1:
                    return l[0]
        return -1
        
        
        return 20190301
        