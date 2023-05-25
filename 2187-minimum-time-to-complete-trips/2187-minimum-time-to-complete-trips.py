class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, max(time) * totalTrips
        
        while left < right:
            mid = (left + right) // 2
            actual_trips = 0
            
            for t in time:
                actual_trips += mid // t
            
            if actual_trips >= totalTrips:
                right = mid
            else:
                left = mid + 1
        return left
        