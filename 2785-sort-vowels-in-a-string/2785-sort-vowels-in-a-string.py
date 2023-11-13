class Solution:
    def sortVowels(self, s: str) -> str:
        pq = []
        for ch in s:
            if ch.lower() in ['a','e','i','o','u']:
                heapq.heappush(pq, (ord(ch), ch))
                
        res = ""
        for ch in s:
            if ch.lower() in ['a','e','i','o','u']:
                res += heapq.heappop(pq)[1]
            else:
                res += ch
        return res
        