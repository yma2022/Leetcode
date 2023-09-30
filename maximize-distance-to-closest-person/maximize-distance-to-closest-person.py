class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_dist = 0
        
        for i in range(len(seats)):
            if seats[i] == 1:
                continue
            l, r = i, i
            dist = 0
            while l >=0 or r < len(seats):
                l -= 1
                r += 1
                dist += 1
                if l >= 0 and seats[l] == 1 or r < len(seats) and seats[r] == 1:
                    break
            max_dist = max(max_dist, dist)
            
        return max_dist
        