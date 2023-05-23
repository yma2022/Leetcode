class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remain = dict()
        for t in time:
            r = t%60
            if r in remain:
                remain[r] += 1
            else:
                remain[r] = 1
        print(remain)
        res = 0
        for key in remain:
            if key == 0 or key == 30:
                res += (remain[key] - 1) * remain[key]
            elif 60-key in remain:
                res += remain[key] * remain[60-key]
            print(res)
        res = res // 2
        return res