class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
#         graph = collections.defaultdict(set)
        
#         for c in connections:
#             graph[c[0]].add(c[1])
#             graph[c[1]].add(c[0])
            
#         def dfs(x):
#             if visited[x]:
#                 return
#             visited[x] = True
#             for nx in graph[x]:
#                 if not visited[nx]:                    
#                     dfs(nx)
#         count = 0
#         visited = [False for _ in range(n)]
#         for i in range(n):
#             if not visited[i]:
#                 count += 1
#                 dfs(i)    
#         return count -1 if len(connections) >= n - 1 else -1
        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]
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
            elif rank[u] == rank[v] and u != v:
                parent[v] = u
                rank[u] += 1
        ans = n  
        for c in connections:
            if find(c[0]) != find(c[1]):
                ans -= 1
                join(c[0], c[1])
            
        return ans - 1 if len(connections) >= n - 1 else -1
        