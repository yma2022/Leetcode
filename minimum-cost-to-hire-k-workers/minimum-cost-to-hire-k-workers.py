class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([(w / q, w, q) for w, q in zip(wage, quality)])
        
        cost, team, sumq = float('inf'), [], 0
        
        for ratio, w, q in workers:
            heapq.heappush(team, -q)
            sumq += q
            if len(team) > k:
                sumq += heapq.heappop(team)
            if len(team) == k:
                cost = min(cost, sumq * ratio)
        return cost
        