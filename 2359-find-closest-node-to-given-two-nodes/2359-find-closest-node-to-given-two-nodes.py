class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dist1 = [float('inf') for _ in range(n)]
        dist2 = [float('inf') for _ in range(n)]
        
        visit1 = [False for _ in range(n)]
        visit2 = [False for _ in range(n)]
        
        def dfs(node, dist, visit):
            visit[node] = True
            nei = edges[node]
            if nei != -1 and not visit[nei]:
                dist[nei] = 1 + dist[node]
                dfs(nei, dist, visit)
        dist1[node1] = 0
        dist2[node2] = 0
        dfs(node1, dist1, visit1)
        dfs(node2, dist2, visit2)
        
        minDistNode = -1
        minDistTillNow = float('inf')
        
        for i in range(n):
            if minDistTillNow > max(dist1[i], dist2[i]):
                minDistNode = i
                minDistTillNow = max(dist1[i], dist2[i])
                
        return minDistNode
            