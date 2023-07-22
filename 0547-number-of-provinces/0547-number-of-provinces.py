class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # graph = collections.defaultdict(list)
        # for i in range(len(isConnected)):
        #     for j in range(len(isConnected[0])):
        #         if isConnected[i][j] == 1:
        #             graph[i].append(j)
        # visited = [False] * len(isConnected)
        # def dfs(city):
        #     for c in graph[city]:
        #         if visited[c]:
        #             continue
        #         if len(graph[c]) == 1:
        #             continue
        #         visited[c] = True
        #         dfs(c)
        #     return
        # count = 0
        # for i in range(len(isConnected)):
        #     if not visited[i]:
        #         dfs(i)
        #         count += 1
        # return count
        visited = set()
        count = 0
        def dfs(city, visited):
            for new_city, is_friend in enumerate(M[city]):
                if new_city not in visited and is_friend:
                    visited.add(new_city)
                    dfs(new_city, visited)
                    
        for city in range(len(M)):
            if city not in visited:
                visited.add(city)
                count+=1
                dfs(city, visited)
        return count
        