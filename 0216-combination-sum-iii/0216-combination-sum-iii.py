class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(curr, path, results):
            if sum(path) > n:
                return
            if len(path) == k:
                if sum(path) == n:
                    results.append(path[:])
                return
            for i in range(curr, 11-(k-len(path))):
                path.append(i)
                backtrack(i+1, path, results)
                path.pop()
        results = []
        backtrack(1, [], results)
        return results
        