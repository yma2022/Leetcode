class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right = 0, 0
        window_sum = 0
        ans = -inf
        while right < len(nums):
            window_sum += nums[right]
            if right - left + 1 >= k:
                if window_sum > ans * k:
                    ans = window_sum / k
                window_sum -= nums[left]
                left += 1
            right += 1
        return ans
        