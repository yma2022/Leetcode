class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        s = 0
        for num in nums:
            s += num
            res.append(s)
        return res