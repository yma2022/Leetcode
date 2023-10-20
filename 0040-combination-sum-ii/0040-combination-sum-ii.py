class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        def backtrack(curr, path, results):
            if sum(path[:]) > target:
                return
            if sum(path[:]) == target:
                results.append(path[:])
                return
            for i in range(curr, n):
                if i > curr and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i+1, path, results)
                path.pop()
        candidates.sort()
        res = []       
        backtrack(0, [], res)
        return res
        