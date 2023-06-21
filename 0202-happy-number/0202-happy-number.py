class Solution:
    def isHappy(self, n: int) -> bool:
        hashmap = []
        while n not in hashmap:
            hashmap.append(n)
            num = 0
            while n:
                r = n % 10
                num += r * r
                n = n // 10
            n = num
            if n == 1:
                return True
        return False
        