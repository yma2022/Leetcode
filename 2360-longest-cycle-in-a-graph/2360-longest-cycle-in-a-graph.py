class Solution:
    def __init__(self):
        self.ans = -1
    def longestCycle(self, edges: List[int]) -> int:
        
        def dfs(node, edges, dist, visit):
            visit[node] = True
            neighbor = edges[node]
            if neighbor != -1 and not visit[neighbor]:
                dist[neighbor] = dist[node] + 1
                dfs(neighbor, edges, dist, visit)
            elif neighbor != -1 and neighbor in dist:
                self.ans = max(self.ans, dist[node] - dist[neighbor] + 1)
                
        n = len(edges)
        visit = [False] * n
        for i in range(n):
            if not visit[i]:
                dist = collections.defaultdict()
                dist[i] = 1
                dfs(i, edges, dist, visit)
                
        return self.ans
            
        