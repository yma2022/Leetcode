class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
        visited = [False] * len(isConnected)
        def dfs(city):
            for c in graph[city]:
                if visited[c]:
                    continue
                if len(graph[c]) == 1:
                    continue
                visited[c] = True
                dfs(c)
            return
        count = 0
        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(i)
                count += 1
        return count
        