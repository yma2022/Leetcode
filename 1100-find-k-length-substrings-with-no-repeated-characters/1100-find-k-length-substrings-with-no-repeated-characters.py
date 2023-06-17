class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        left, right = 0, 0
        n = len(s)
        ans = 0
        while right < n:                
            if right - left + 1 >= k:
                subs = s[left: right+1]
                # print(subs) if len(set(subs)) == k else 0
                ans += 1 if len(set(subs)) == k else 0
                left += 1
            right += 1
        return ans