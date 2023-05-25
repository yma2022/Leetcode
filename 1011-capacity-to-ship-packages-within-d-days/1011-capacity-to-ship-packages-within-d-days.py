class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left <= right:
            mid = (left + right) // 2
            #need is delivery days
            #curr is current sum weights of delivered packs
            need, curr = 1, 0
            for weight in weights:
                if curr + weight > mid:
                    need += 1
                    curr = 0
                curr += weight
            if need <= days:
                right = mid - 1
            else:
                left = mid + 1
                
        return left