class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        min_array = [-1] * n
        min_array[0] = nums[0]
        for i in range(1, n):
            min_array[i] = min(min_array[i - 1], nums[i])
        k = n   
        for j in range(n - 1, -1, -1):
            if nums[j] <= min_array[j]:
                continue
            while k < n and nums[k] <= min_array[j]:
                k += 1
            if k < n and nums[k] < nums[j]:
                return True
            k -= 1
            nums[k] = nums[j]
            # print(nums)
        
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