class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.sort()
        sorted_people = sorted(people)
        pq = []
        d = {}
        i = 0
        for p in sorted_people:
            while i < len(flowers) and flowers[i][0] <= p:
                heapq.heappush(pq, flowers[i][1])
                i += 1
            while pq and pq[0] < p:
                heapq.heappop(pq)
            
            d[p] = len(pq)
        return [d[p] for p in people]
        