class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wList = s.split()
        return len(wList[-1])
        