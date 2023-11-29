class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        rev = [1] * n
        for i in range(1, n):
            res[i] = nums[i-1] * res[i-1]
        for j in range(n-2, -1, -1):
            rev[j] = nums[j+1] * rev[j+1]
        for i in range(n):
            res[i] = res[i] * rev[i]
        return res
            