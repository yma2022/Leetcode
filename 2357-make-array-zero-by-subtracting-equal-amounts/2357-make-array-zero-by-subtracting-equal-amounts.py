class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        hashmap = set()
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            if nums[i] not in hashmap:
                count += 1
                hashmap.add(nums[i])
            else:
                continue
            
        return count
        