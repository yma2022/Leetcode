class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binarySearch(sub, num):
            left, right = 0, len(sub) - 1            
            while left < right:
                mid = (left + right) // 2
                if sub[mid] == num:
                    return mid
                if sub[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        sub = []
        sub.append(nums[0])
        
        for num in nums:
            if num > sub[-1]:
                sub.append(num)
            else:
                j = binarySearch(sub, num)
                sub[j] = num
                
        return len(sub)
    
        