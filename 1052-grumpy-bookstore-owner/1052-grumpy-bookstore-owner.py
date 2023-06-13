class Solution:
                
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        left, right = 0, 0
        window_sum = 0
        ans = 0
        while right < len(customers):
            if grumpy[right] == 1:
                window_sum += customers[right]
            if right - left + 1 > minutes:
                if grumpy[left] == 1:
                    window_sum -= customers[left]
                left += 1
            right += 1
            ans = max(ans, window_sum)
        
        for i in range(len(customers)):
            ans += customers[i] if grumpy[i] == 0 else 0
        return ans
        