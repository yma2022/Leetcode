class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        
        for num in nums:
            heapq.heappush(pq, num)
        # print(pq)
        while len(pq) > k:
            heapq.heappop(pq)           
          
        return pq[0]