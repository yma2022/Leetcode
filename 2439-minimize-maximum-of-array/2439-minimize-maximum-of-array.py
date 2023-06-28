class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        def check_arr(val):
            carry = 0
            for i in range(len(nums) - 1, 0, -1):
                if nums[i] + carry > val:
                    carry = (nums[i] + carry) - val
                else:
                    carry = 0
            return True if nums[0] + carry <= val else False
        
        left, right = 0, max(nums) + 1
        while left < right:
            mid = (left + right) // 2
            check = check_arr(mid)
            if check:
                right = mid
            else:
                left = mid + 1
        return left
        
        