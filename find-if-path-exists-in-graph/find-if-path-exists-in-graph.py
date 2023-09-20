class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = collections.defaultdict(set)
        for e in edges:
            g[e[0]].add(e[1])
            g[e[1]].add(e[0]) 
        def dfs(src, dst):
            nonlocal seen
            if src == dst:
                return True
            if src not in seen:
                seen.add(src)
                for nei in g[src]:
                    if dfs(nei, dst):
                        return True
            return False
        
        seen = set()
        return dfs(source, destination)
        