class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(curr, comb, res):
            if sum(comb) > target:
                return
            if sum(comb) == target:
                res.append(comb[:])
                return
            
            for i in range(curr, len(candidates)):
                if i > curr and candidates[i] == candidates[i-1]:
                    continue
                comb.append(candidates[i])
                backtrack(i + 1, comb, res)
                comb.pop()
        candidates.sort()
        results = []
        backtrack(0, [], results)
        return results
                