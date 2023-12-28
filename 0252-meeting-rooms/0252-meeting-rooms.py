class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x:x[1])
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[i-1][1]:
                continue
            else:
                return False
        return True