class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if (sx, sy) == (fx, fy):
            return t == 0 or t > 1
        min_step = max(abs(fx - sx), abs(sy - fy))               
        return t >= min_step