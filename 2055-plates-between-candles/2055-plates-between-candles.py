class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        res = []
        candles = []
        for i in range(len(s)):
            if s[i] == '|':
                candles.append(i)
        def binarySearch(num, array):
            l, r = 0, len(array) - 1
            while l <= r:
                mid = (l + r) // 2
                if array[mid] < num:
                    l = mid + 1
                elif array[mid] > num:
                    r = mid - 1
                else:
                    return mid
            return l
        # print(candles)
        for q in queries:
            start = binarySearch(q[0], candles)
            end = binarySearch(q[1], candles)
            if end >= len(candles) or candles[end] > q[1]:
                end -= 1
            # print(start, end)
            if start >= end:
                count = 0
            else:
                count = candles[end] - candles[start] - (end - start)
            res.append(count)
            
        return res
        