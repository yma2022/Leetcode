class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = dict()
        for i in range(len(nums)):
            if nums[i] in check:
                return [check[nums[i]], i]
            check[target - nums[i]] = i