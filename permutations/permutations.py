class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(p):
            if len(p) == len(nums):
                res.append(p[:])
                return
            for i in range(len(nums)):
                if nums[i] not in p:
                    p.append(nums[i])
                    backtrack(p)
                    p.pop()
                    
                    
                
        res = []
        backtrack([])
        return res