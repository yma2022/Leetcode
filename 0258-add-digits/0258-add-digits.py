class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            tmp = 0
            for d in str(num):
                tmp += int(d)
                
            num = tmp
            if 0 <= num < 10:
                break
        return num
        