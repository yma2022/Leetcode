class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def get_count(x):
            total = 0
            count = 1
            for num in nums:
                if total + num > x:
                    count += 1
                    total = num
                else:
                    total += num
            return count

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if get_count(mid) > k:
                left = mid + 1
            else:
                right = mid
        return left        