class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        pq = []
        
        for x in range(1, int(n**0.5)+1):
            if n%x == 0:
                heapq.heappush(pq, -x)
                if len(pq) > k:
                    heapq.heappop(pq)
                if x != n//x:
                    heapq.heappush(pq, -n//x)
                    if len(pq) > k:
                        heapq.heappop(pq)
        return -heapq.heappop(pq) if k == len(pq) else -1
        