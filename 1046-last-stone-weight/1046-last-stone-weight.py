class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-x for x in stones]
        heapq.heapify(pq)
        
        while len(pq) > 1:
            print(pq)
            stone1 = heapq.heappop(pq)
            stone2 = heapq.heappop(pq)
            if stone1 == stone2:
                continue
            heapq.heappush(pq, stone1 - stone2)
            
        return -pq[0] if pq else 0
        