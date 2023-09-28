class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = "".join(s.split("-"))
        chars = chars.upper()
        if len(chars) <= k:
            return chars
        n = len(chars)
        curr = n
        res = ""
        while len(chars[:curr]) > k:
            res = "-" + chars[curr - k:curr] + res
            curr -= k
        res = chars[:curr] + res
        return res
        