class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p0 = 0
        p1 = n - 1
        curr = 0
        while curr <= p1:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p1] = nums[p1] , nums[curr]
                p1 -= 1
            else:
                curr += 1
                        