class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        rooms = []
        
        intervals.sort(key = lambda x: x[0])
        heapq.heappush(rooms, intervals[0][1])
        
        for i in intervals[1:]:
            
            if rooms[0] <= i[0]:
                heapq.heappop(rooms)
                
            heapq.heappush(rooms, i[1])
            
        return len(rooms)
        