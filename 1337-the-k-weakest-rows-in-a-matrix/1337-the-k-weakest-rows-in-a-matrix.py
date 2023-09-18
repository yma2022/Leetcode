class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        pq = []
        res = []
        
        for i in range(len(mat)):
            d = sum(mat[i])
            heapq.heappush(pq, (d, i))
        while len(pq) > len(mat) - k:
            res.append(heapq.heappop(pq)[1])                   
        return res