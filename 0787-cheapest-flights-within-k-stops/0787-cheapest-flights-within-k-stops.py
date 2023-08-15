class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        seen = set()
        graph = collections.defaultdict(list)
        for f in flights:
            graph[f[0]].append([f[1], f[2]])
            
        q = deque()
        q.append([src, 0])
        stops = 0
        dist = [float('inf') for _ in range(n)]
        while q and stops <= k:
            length = len(q)
            while length :
                length -= 1
                node, d = q.popleft()
                for nei, price in graph[node]:
                    if price + d < dist[nei]:
                        dist[nei] = price + d
                        q.append([nei, dist[nei]])
            stops += 1
            
        return -1 if dist[dst] == float('inf') else dist[dst]
                