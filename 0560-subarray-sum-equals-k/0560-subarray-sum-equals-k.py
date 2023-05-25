class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        checkmap = dict()        
        count = 0
        curr_sum = 0
        checkmap[0] = 1
        for i in range(len(nums)):
            # print(checkmap)
            curr_sum += nums[i]
            if curr_sum-k in checkmap:
                count += checkmap[curr_sum-k]
            if curr_sum in checkmap:
                checkmap[curr_sum] = checkmap[curr_sum] + 1
            else:
                checkmap[curr_sum] = 1
        return count
        
            