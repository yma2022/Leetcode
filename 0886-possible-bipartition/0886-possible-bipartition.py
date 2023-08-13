class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(node, node_color):
            color[node] = node_color
            for nei in graph[node]:
                if color[nei] == color[node]:
                    return False
                if color[nei] == -1:
                    if not dfs(nei, 1 - node_color):
                        return False
            return True
        
        graph = [[] for _ in range(n + 1)]
        for d in dislikes:
            graph[d[0]].append(d[1])
            graph[d[1]].append(d[0])
            
        color = [-1] * (n + 1)
        for i in range(1, n + 1):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
                
        return True