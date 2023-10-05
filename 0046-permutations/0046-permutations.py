class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(seen, path, res):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for num in nums:
                if num in seen:
                    continue
                seen.add(num)
                path.append(num)
                backtrack(seen, path, res)
                path.pop()
                seen.remove(num)
        
        path, results = [], []
        seen = set()
        backtrack(seen, path, results)
        return results