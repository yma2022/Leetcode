class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for e in edges:
            graph[e[0]].append(e[1])
            
        def dfs(graph, node, dst, states):
            if states[node] != 0:
                return states[node] == 2
            
            if len(graph[node]) == 0:
                return node == dst
            states[node] = 1
            for next_node in graph[node]:
                if not dfs(graph, next_node, dst, states):
                    return False
            states[node] = 2
            return True
        return dfs(graph, source, destination, [0] * n)
        