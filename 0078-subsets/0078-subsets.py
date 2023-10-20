class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, path, results):
            if len(path) <= len(nums):
                results.append(path[:])
                
            for i in range(curr, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path, results)
                path.pop()
        res = []
        backtrack(0, [], res)
        return res
        