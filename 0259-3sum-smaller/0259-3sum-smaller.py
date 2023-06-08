class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n):
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < target:
                    res += (right - left)
                    left += 1
                else:
                    right -= 1
        return res