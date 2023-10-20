class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def backtrack(path, seen, results):
            if len(path) == n:
                results.append(path[:])
                return
            for i in range(n):
                if nums[i] in seen:
                    continue
                path.append(nums[i])
                seen.add(nums[i])
                backtrack(path, seen, results)
                seen.remove(nums[i])
                path.pop()
        seen = set()
        res = []
        backtrack([], seen, res)
        return res
        