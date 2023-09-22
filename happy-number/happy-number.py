class Solution:
    def isHappy(self, n: int) -> bool:
        hashmap = set()
        while n not in hashmap:
            hashmap.add(n)
            next_n = 0
            while n > 0:
                next_n += (n % 10)**2
                n //= 10
            # print(next_n)
            n = next_n
            if n == 1:
                return True
        return False
        