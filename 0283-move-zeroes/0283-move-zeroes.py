class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = 0
        n = len(nums)
        while p2 < n:
            if not nums[p1]:
                if not nums[p2]:
                    p2 += 1
                else:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                    p1 += 1
            else:
                p1 += 1
                if p1 > p2:
                    p2 = p1
                