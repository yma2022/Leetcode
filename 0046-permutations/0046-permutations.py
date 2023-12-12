class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, res, seen):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(0, len(nums)):
                if i in seen:
                    continue
                path.append(nums[i])
                seen.add(i)
                backtrack(path, res, seen)
                seen.remove(i)
                path.pop()
        res = []
        seen = set()
        backtrack([], res, seen)
        return res