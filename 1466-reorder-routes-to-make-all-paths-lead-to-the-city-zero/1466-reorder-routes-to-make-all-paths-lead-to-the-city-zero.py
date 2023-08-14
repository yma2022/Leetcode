class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.count = 0
        graph = collections.defaultdict(list)
        for c in connections:
            graph[c[0]].append((c[1], 1))
            graph[c[1]].append((c[0], 0))
        
        def dfs(node, parent):
            for child, sign in graph[node]:
                if child != parent:
                    self.count += sign
                    dfs(child, node)
        
        dfs(0, -1)
        return self.count
        