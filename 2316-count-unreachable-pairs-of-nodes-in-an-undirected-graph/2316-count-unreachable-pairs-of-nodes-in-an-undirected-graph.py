class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        
        
        def dfs(x):
            visited[x] = True
            count = 1
            for nx in graph[x]:
                if not visited[nx]:
                    count += dfs(nx)
            return count
        
        res = 0
        count = 0
        remain = n
        visited = [False for _ in range(n)]
        for i in range(n):            
            if not visited[i]:
                count = dfs(i)
                res += count * (remain - count)
                remain -= count
                
        return res
        