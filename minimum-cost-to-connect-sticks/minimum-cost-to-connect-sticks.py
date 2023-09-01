class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        pq = sticks
        heapq.heapify(pq)
        
        cost = 0
        
        while len(pq) > 1:
            stick1 = heapq.heappop(pq)
            stick2 = heapq.heappop(pq)
            
            new_stick = stick1 + stick2
            cost += new_stick
            heapq.heappush(pq, new_stick)
        
        return cost
            
        