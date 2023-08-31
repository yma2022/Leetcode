class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        pq = []
        heapq.heapify(pq)
        
        for i in range(len(mat)):
            d = Counter(mat[i])
            heapq.heappush(pq, (d[1], i))
            
        res = []
        for i in range(k):
            res.append(heapq.heappop(pq)[1])
        
        return res