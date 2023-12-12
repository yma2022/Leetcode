class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(curr, path, res):
            if sum(path) >= target:
                if sum(path) == target:
                    res.append(path[:])
                return
            
            for i in range(curr, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, res)
                path.pop()
        res = []
        backtrack(0, [], res)
        return res