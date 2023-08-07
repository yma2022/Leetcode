class Solution:
    t = 0
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = collections.defaultdict(list)
        
        for i in range(n):
            graph[manager[i]].append((i, informTime[i]))

        def dfs(x, t):
            self.t = max(self.t, t)
            for nx, nt in graph[x]:
                if nx in graph:
                    dfs(nx, t + nt)
                  
        dfs(-1, 0)
        
        return self.t
        