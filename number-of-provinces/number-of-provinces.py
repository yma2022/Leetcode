class UnionFind:
    def __init__(self, size):
        self.parent= [i for i in range(size)]
        self.rank = [1] * size
    def find(self, u):
        if u == self.parent[u]:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            if self.rank[u] > self.rank[v]:
                self.parent[v] = u
            elif self.rank[v] > self.rank[u]:
                self.parent[u] = v
            else:
                self.parent[v] = u
                self.rank[u] += 1
                
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        uf = UnionFind(len(M))
        ans = len(M)
        for i in range(len(M)):
            for j in range(i+1, len(M[0])):
                if M[i][j] and uf.find(i) != uf.find(j):
                    uf.union(i, j)
                    ans -= 1
        print(uf.rank)
        return ans
            
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
#         visited = set()
#         count = 0
#         def dfs(city, visited):
#             visited.add(city)
#             for new_city, is_friend in enumerate(M[city]):
#                 if new_city not in visited and is_friend:                    
#                     dfs(new_city, visited)
                    
#         for city in range(len(M)):
#             if city not in visited:
#                 count+=1
#                 dfs(city, visited)
#         return count
################################################################################################
            
        