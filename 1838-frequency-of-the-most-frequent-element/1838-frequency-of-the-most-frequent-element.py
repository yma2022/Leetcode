class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        n = len(nums)
        ans = 1
        sum = 0
        for j in range(n):
            sum += nums[j]
            while ((j - i + 1) * nums[j] - sum > k):
                sum -= nums[i]
                i += 1
            ans = max(ans , j - i + 1)
        return ans