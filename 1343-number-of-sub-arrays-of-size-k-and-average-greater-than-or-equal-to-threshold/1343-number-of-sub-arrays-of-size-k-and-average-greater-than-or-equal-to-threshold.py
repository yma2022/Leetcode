class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        left = 0
        right = 0
        window_sum = 0
        res = 0

        while right < len(arr):
            window_sum += arr[right]
            
            if right - left + 1 >= k:
                if window_sum >= k * threshold:
                    res += 1
                window_sum -= arr[left]
                left += 1

            right += 1
            
        return res
        