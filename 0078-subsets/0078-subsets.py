class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, k, subset, res):
            if len(subset) == k:
                res.append(subset[:])
                return
            for i in range(curr, len(nums)):
                subset.append(nums[i])
                backtrack(i+1, k, subset, res)
                subset.pop()
                
        results = []
        for i in range(len(nums) + 1):
            backtrack(0, i, [], results)
        return results
            
            
        