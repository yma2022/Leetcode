class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        
        for num in nums:
            # print(pq)
            heapq.heappush(pq, num)
            if len(pq) > k:
                heapq.heappop(pq)
          
        return pq[0]