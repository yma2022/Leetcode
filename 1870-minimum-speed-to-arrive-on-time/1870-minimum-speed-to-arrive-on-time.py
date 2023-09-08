class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def totalTime(dist, speed):
            t = 0
            for i in range(len(dist) - 1):
                if dist[i] % speed != 0:
                    t += dist[i] // speed + 1
                else:
                    t += dist[i] // speed
            t += dist[-1] / speed
            return t
        
        l, r = 1, max(dist) * 100
        
        while l < r:
            mid = (l + r) // 2
            if totalTime(dist, mid) > hour:
                l = mid + 1
            else:
                r = mid                
        return l if totalTime(dist, l) <= hour else -1