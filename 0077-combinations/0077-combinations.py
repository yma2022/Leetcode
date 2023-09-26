class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(n, k, startIndex, path):
            if len(path) == k:
                res.append(path[:])
            for i in range(startIndex, n + 1):
                path.append(i)
                backtrack(n, k, i + 1, path)
                path.pop()
        res = []
        backtrack(n, k, 1, [])
        return res