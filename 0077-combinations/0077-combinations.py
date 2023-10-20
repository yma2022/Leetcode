class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(curr, path, results):
            if len(path) == k:
                results.append(path[:])
                return
            for i in range(curr, n+1):
                path.append(i)
                backtrack(i+1, path, results)
                path.pop()
                
        res = []
        backtrack(1, [], res)
        return res
        