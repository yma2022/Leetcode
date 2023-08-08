class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        
        for c in connections:
            graph[c[0]].add(c[1])
            graph[c[1]].add(c[0])
            
        def dfs(x):
            if visited[x]:
                return
            visited[x] = True
            for nx in graph[x]:
                if not visited[nx]:                    
                    dfs(nx)
        count = 0
        visited = [False for _ in range(n)]
        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)    
        return count -1 if len(connections) >= n - 1 else -1
        