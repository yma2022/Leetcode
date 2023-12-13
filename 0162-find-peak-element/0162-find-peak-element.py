class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = max(nums)
        return nums.index(n)
        