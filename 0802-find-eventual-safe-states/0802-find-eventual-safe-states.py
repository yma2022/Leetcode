class Solution:    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = {}
        
        def dfs(x):
            if x in safe:
                return safe[x]
            safe[x] = False
            for nei in graph[x]:
                if not dfs(nei):
                    return False
            safe[x] = True
            return True
            
            
            
        res = []   
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)                
        return res
        