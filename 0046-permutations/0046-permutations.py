class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, res):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack(path, res )
                path.pop()
                
        res = []
        backtrack([], res)
        return res