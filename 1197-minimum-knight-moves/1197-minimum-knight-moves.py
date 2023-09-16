class Solution:
    def minKnightMoves(self, fx: int, fy: int) -> int:
        q = deque([(0, 0)])
        seen = set()
        level = 0
        res = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                if (x, y) == (fx, fy):
                    return level
                for dx, dy in [[1,2], [2,1], [-1,2], [-2,1], [-1,-2], [-2,-1], [1,-2], [2,-1]]:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) not in seen:
                        seen.add((nx, ny))
                        q.append((nx, ny))
            level += 1
        