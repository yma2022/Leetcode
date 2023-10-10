class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        new_nums = sorted(set(nums))
        for i in range(len(new_nums)):
            # l = new_nums[i]
            # r = l + n - 1
            insert = new_nums[i] + n - 1
            l, r = 0, len(new_nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if new_nums[mid] <= insert:
                    l = mid + 1
                else:
                    r = mid - 1
            j = l
            count = j - i
            ans = min(ans, n - count)
        return ans
        
        