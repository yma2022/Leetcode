class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:        
        left, right = 0, max(nums) + 1
        while left < right:
            mid = (left + right) // 2
            carry = 0
            for i in range(len(nums) - 1, 0, -1):                
                if nums[i] + carry > mid:
                    carry = (nums[i] + carry) - mid
                else:
                    carry = 0
            if nums[0] + carry > mid:
                left = mid + 1
            else:
                right = mid

        return left
        