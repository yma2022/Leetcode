class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        start = lower
        for num in nums:
            if start >= num:
                start = max(start, num + 1)
                continue
            end = min(num - 1, upper)
            if start > end:
                continue
            print(num, start, end)
            res.append([start, end])
            start = max(start, num + 1)
        if start <= upper:
            res.append([start, upper])
        return res
            
            