class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            time = 0
            for pile in piles:
                t = pile // mid
                time += t if pile % mid == 0 else t + 1
            
            if time > h:
                left = mid + 1
            else:
                right = mid
        return left