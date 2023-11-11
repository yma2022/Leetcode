class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def calDays(capacity):
            day = 0
            curr = 0
            for w in weights:
                if curr + w > capacity:
                    day += 1
                    curr = 0
                curr += w
            return day
        l, r = max(weights), sum(weights)
        
        while l <= r:
            mid = (l + r) // 2
            if calDays(mid) < days:
                r = mid - 1
            else:
                l = mid + 1
        return l
            
        