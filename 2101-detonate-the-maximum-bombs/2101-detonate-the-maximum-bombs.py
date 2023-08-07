class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        n = len(bombs)
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi, ri = bombs[i]
                xj, yj, rj = bombs[j]
                dist = ((xi-xj)**2 + (yi-yj)**2)**0.5
                if dist <= ri:
                    graph[i].add(j)
                    
        def dfs(i):
            visited.add(i)
            for b in graph[i]:
                if b not in visited:
                    dfs(b)
            return len(visited)
            
            
        res = 0
        for i in range(n):
            visited = set()
            res = max(res, dfs(i))
            
        return res
        