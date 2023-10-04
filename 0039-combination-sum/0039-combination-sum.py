class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(curr, comb, results):
            if sum(comb) > target:
                return
            if sum(comb) == target:
                results.append(comb[:])
                return
            
            for i in range(curr, len(candidates)):
                comb.append(candidates[i])
                backtrack(i, comb, results)
                comb.pop()
        results = []
        backtrack(0, [], results)
        return results
        