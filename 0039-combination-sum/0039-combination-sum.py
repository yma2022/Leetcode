class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        def backtrack(curr, path, results):
            if sum(path[:]) > target:
                return
            if sum(path[:]) == target:
                results.append(path[:])
                return
            
            for i in range(curr,n):
                path.append(candidates[i])
                backtrack(i, path, results)
                path.pop()
        res = []    
        backtrack(0, [], res)
        return res
        