class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[1])
        res = []
        for i in intervals:
            while res and i[0] <= res[-1][1]:
                i[0] = min(i[0], res[-1][0]) 
                i[1] = max(i[1], res[-1][1])
                res.pop()
            res.append(i)
        return res
        