class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pq = []
        for i in range(min(k, n)):
            pq.append((matrix[i][0], i, 0))
            
        heapq.heapify(pq)
        
        while k:
            ele, i, j = heapq.heappop(pq)
            if j < n - 1:
                heapq.heappush(pq, (matrix[i][j+1], i, j + 1))
            k -= 1
                
        return ele