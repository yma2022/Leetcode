class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        def totalT(k, piles):
            time = 0
            for p in piles:
                time += (p // k) if (p % k == 0) else (p // k + 1)
            return time
        while left < right:
            mid = (left + right) // 2
            time = totalT(mid, piles)
            if time > h:
                left = mid + 1
            else:
                right = mid
                
        return left