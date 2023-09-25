class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = [0] * 26
        for c1, c2 in zip(s, t):
            d[ord(c1) - ord('a')] += 1
            d[ord(c2) - ord('a')] -= 1

        return chr(d.index(-1) + ord('a')) if -1 in d else t[-1]