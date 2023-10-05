class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(seen, path, res):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i, num in enumerate(nums):
                if i > 0 and num == nums[i-1] and not seen[i-1] or seen[i]:
                    continue
                seen[i] = True
                path.append(num)
                backtrack(seen, path, res)
                path.pop()
                seen[i] = False
        
        path, results = [], []
        seen = [False] * len(nums)
        nums.sort()
        backtrack(seen, path, results)
        return results