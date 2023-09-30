class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        s3 = float('-inf')
        stack = []
        for i in range(n - 1, -1, -1):
            if nums[i] < s3:
                return True
            else:
                while stack and nums[i] > stack[-1]:
                    s3 = stack[-1]
                    stack.pop()
            stack.append(nums[i])
        return False

            
#         min_point_after_last_peak = 0
#         intervals = []
        
#         for i in range(n):
#             if nums[i] < nums[i - 1]:
#                 if min_point_after_last_peak < i - 1:
#                     intervals.append((nums[min_point_after_last_peak], nums[i - 1]))
#                 min_point_after_last_peak = i
                
#             for interval in intervals:
#                 if interval[0] < nums[i] < interval[1]:
#                     return True
#         return False