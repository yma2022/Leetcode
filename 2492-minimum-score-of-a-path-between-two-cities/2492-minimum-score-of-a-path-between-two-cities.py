class Solution:
    def __init__(self):
        self.res = float('inf')
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for r in roads:
            graph[r[0]].append((r[1],r[2]))
            graph[r[1]].append((r[0],r[2]))
        
        visit = [False for _ in range(n+1)]
        def dfs(x):
            visit[x] = True
            for i in range(len(graph[x])):
                nx, dist = graph[x][i]
                self.res = min(self.res, dist)
                if not visit[nx]:
                    dfs(nx)
        
        dfs(1)
        return self.res
        