class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(curr, path, res):
            if len(path) == k:
                res.append(path[:])
                return
            
            for i in range(curr, n+1):
                path.append(i)
                backtrack(i+1, path, res)
                path.pop()
                
        res = []
        backtrack(1, [], res)
        return res
        
        