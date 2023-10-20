class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def backtrack(curr, path, seen, results):
            if len(path) == n:
                results.append(path[:])
                return
            for i in range(n):
                if i in seen:
                    continue
                if i > 0 and nums[i] == nums[i-1] and (i-1) not in seen:
                    continue
                seen.add(i)
                path.append(nums[i])
                backtrack(i+1, path, seen, results)
                path.pop()
                seen.remove(i)
        nums.sort()
        seen = set()
        res = []
        backtrack(0, [], seen, res)
        return res
        