class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        size = n - k
        left, right = 0, 0
        window_sum = 0
        total = sum(cardPoints)
        ans = 0
        if not size:
            return total
        
        while right < n:
            window_sum += cardPoints[right]
            if right - left + 1 >= size:
                ans = window_sum if not ans else min(window_sum, ans)
                window_sum -= cardPoints[left]                
                left += 1
            
            right += 1            
        
        ans = total - ans
        return ans