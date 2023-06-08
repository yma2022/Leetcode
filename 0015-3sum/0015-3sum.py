class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Hashmap
        # res, dups = set(), set()
        # seen = {}
        # for i, val1 in enumerate(nums):
        #     if val1 not in dups:
        #         dups.add(val1)
        #         for j, val2 in enumerate(nums[i+1:]):
        #             complement = -val1 - val2
        #             if complement in seen and seen[complement] == i:
        #                 res.add(tuple(sorted((val1, val2, complement))))
        #             seen[val2] = i
        # return res
        
        n = len(nums)
        nums.sort()
        ans = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                while left < right and left > i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and right < n - 1 and nums[right + 1] == nums[right]:
                    right -= 1
                if left < right and nums[i] + nums[left] + nums[right] == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return ans