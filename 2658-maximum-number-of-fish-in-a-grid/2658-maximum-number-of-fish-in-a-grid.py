class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        seen = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and not seen[r][c] and grid[r][c]):
                return 0
            seen[r][c] = True
            return (grid[r][c] + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))