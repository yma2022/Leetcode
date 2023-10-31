class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(curr, path, results):
            if sum(path) == n and len(path) == k:
                results.append(path[:])
                return
            
            for i in range(curr, 10):
                path.append(i)
                backtrack(i+1, path, results)
                path.pop()
                
        res = []
        backtrack(1, [], res)
        return res
        