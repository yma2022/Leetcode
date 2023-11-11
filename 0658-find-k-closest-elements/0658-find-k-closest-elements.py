class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pq = []
        
        for num in arr:
            heapq.heappush(pq, (-abs(num-x), -num))
            while len(pq) > k:
                heapq.heappop(pq)
        res = []       
        while pq:
            res.append(-heapq.heappop(pq)[1])
        return sorted(res)