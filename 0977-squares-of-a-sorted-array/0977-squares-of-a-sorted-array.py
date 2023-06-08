class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0 for _ in range(n)]
        
        left, right = 0, n - 1
        index = n - 1
        while left <= right:                
            if abs(nums[left]) <= abs(nums[right]):
                res[index] = nums[right] ** 2
                right -= 1
            else:
                res[index] = nums[left] ** 2
                left += 1
            index -= 1
        return res
                
                