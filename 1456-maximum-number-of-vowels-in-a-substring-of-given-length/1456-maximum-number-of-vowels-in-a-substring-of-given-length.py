class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        left, right = 0, 0
        ans = 0
        count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        while right < n:
            if s[right] in vowels:
                count += 1
            if right - left + 1 >= k:
                ans = max(ans, count)
                if s[left] in vowels:
                    count -= 1
                left += 1
            
            right += 1
            
        return ans