class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
#         def binarySearch(sub, num):
#             left, right = 0, len(sub) - 1            
#             while left < right:
#                 mid = (left + right) // 2                
#                 if sub[mid] < num:
#                     left = mid + 1
#                 else:
#                     right = mid
#             return left
        
#         sub = []
#         sub.append(nums[0])
        
#         for num in nums:
#             if num > sub[-1]:
#                 sub.append(num)
#             else:
#                 j = binarySearch(sub, num)
#                 sub[j] = num
                
#         return len(sub)
        
        
    
        