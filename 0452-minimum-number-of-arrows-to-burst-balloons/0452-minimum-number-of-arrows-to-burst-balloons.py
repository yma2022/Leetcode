class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        
        common = []
        for p in points:
            while common and p[0] <= common[-1][1]:
                p[0] = max(p[0], common[-1][0])
                p[1] = min([p[1], common[-1][1]])
                common.pop()
                
            common.append(p)
            
        return len(common)
        