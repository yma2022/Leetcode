class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, path, res, seen):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(0, len(nums)):
                if i in seen:
                    continue
                path.append(nums[i])
                seen.add(i)
                backtrack(i+1, path, res, seen)
                seen.remove(i)
                path.pop()
        res = []
        seen = set()
        backtrack(0, [], res, seen)
        return res