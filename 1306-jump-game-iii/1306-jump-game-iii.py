class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        graph = collections.defaultdict(list)
        seen = set()
        for i in range(len(arr)):
            if i - arr[i] >= 0:
                graph[i].append(i - arr[i])
            if i + arr[i] < len(arr):
                graph[i].append(i + arr[i])
                
        def dfs(x):
            if arr[x] == 0:
                return True
            if x in seen:
                return False
            seen.add(x)
            for nx in graph[x]:
                if dfs(nx):
                    return True
                
            return False
                
        return dfs(start)
            
            