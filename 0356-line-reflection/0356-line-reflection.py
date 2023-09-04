class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        points.sort(key = lambda x: x[0])
        const = points[0][0] + points[-1][0]
        for p in points:
            if [const - p[0], p[1]] in points:
                continue            
            return False
        return True
            