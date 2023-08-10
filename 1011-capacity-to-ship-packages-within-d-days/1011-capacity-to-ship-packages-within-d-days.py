class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            total = 0
            time = 1
            for w in weights:                
                if total + w > mid:
                    time += 1
                    total = 0
                total += w
            
            if time <= days:
                right = mid
            else:
                left = mid + 1
            
        return left