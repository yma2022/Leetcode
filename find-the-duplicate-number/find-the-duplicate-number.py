class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        left, right = 1, n
        
        while left < right:
            mid = (left + right) // 2
            cnt = 0
            cnt = sum(num <= mid for num in nums)
            
            if cnt <= mid:
                left = mid + 1
            else:
                 right = mid
        return left
        