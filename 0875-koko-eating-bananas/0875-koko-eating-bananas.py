class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            t = 0
            for p in piles:
                curr = p // mid + 1 if p % mid != 0 else p // mid
                t += curr
            if t > h:
                left = mid + 1
            else:
                right = mid
                
        return left