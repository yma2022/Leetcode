class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums: List[int], left: int, right: int)->List[int]:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            return nums
        
        n = len(nums)
        while k > n:
            k = k % n
        reverse(nums, 0, n-1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)
        