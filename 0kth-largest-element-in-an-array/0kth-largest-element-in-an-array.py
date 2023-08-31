class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        heapq.heapify(pq)
        for num in nums:
            heapq.heappush(pq, num)
            if len(pq) > k:
                heapq.heappop(pq)
        return pq[0]