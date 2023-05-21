class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[1])
        
        merged = []
        for i in range(len(intervals) - 1, -1, -1):
            if not merged or merged[-1][0] > intervals[i][1]:
                merged.append(intervals[i])
            else:
                merged[-1][0] = min(merged[-1][0], intervals[i][0])
                
        return merged 