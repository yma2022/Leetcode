class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(curr, path, results):
            if len(path) == k:
                results.append(path[:])
                return
            for i in range(curr,n+2-(k-len(path))):
                path.append(i)
                backtrack(i+1, path, results)
                path.pop()
        results = []
        backtrack(1, [], results)
        return results
        