class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                if nums[slow] == val:
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
        return slow
        