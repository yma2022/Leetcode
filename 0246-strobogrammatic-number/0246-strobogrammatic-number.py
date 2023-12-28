class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        d = {'6':'9', '8':'8', '9':'6', '0':'0', '1':'1'}
        l, r = 0, len(num) - 1
        while l <= r:
            if num[l] in d and d[num[l]] == num[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
        