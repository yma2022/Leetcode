class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, k, path, res):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(curr, len(nums)):
                if i > curr and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i+1, k, path, res)
                path.pop()
            
            
        nums.sort()
        results = []
        for i in range(len(nums) + 1):
            backtrack(0, i, [], results)
        return results
        