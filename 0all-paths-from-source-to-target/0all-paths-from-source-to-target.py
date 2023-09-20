class Solution:

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.result = []
        self.path = [0]
        
        if not graph: return []
        
        def dfs(root):
            if root == len(graph) - 1:
                self.result.append(self.path[:])
                return
            for node in graph[root]:
                self.path.append(node)
                dfs(node)
                self.path.pop()
                
        dfs(0)
        return self.result