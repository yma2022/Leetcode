class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        curr = n - 1
        k = 0
        while s[curr] == ' ':
            curr -= 1
        while curr >= 0 and s[curr] != ' ':
            curr -= 1
            k += 1
        return k
        