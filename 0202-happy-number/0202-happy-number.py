class Solution:
    def isHappy(self, n: int) -> bool:
        happyNs = set()
        
        while True:
            tmp = 0
            for c in str(n):
                tmp += int(c)**2
            n = tmp
            if n in happyNs:
                break
            happyNs.add(n)
        # print(n)   
        return n == 1
        