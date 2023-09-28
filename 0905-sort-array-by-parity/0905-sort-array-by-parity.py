class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            while nums[l] % 2 == 0:
                l += 1
                if l >= len(nums):
                    return nums
            while nums[r] % 2 == 1:
                r -= 1
                if r <= 0:
                    return nums
            if l < r and nums[l] % 2 == 1 and nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
        return nums
        