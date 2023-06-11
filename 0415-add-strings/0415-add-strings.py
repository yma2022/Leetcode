class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        right_1, right_2 = len(num1) - 1, len(num2) - 1
        l = []
        while right_1 > -1 or right_2 > -1 or carry > 0:
            digit_1 = int(num1[right_1]) if right_1 >=0 else 0
            digit_2 = int(num2[right_2]) if right_2 >=0 else 0
            temp = digit_1 + digit_2 + carry
            carry = temp // 10
            l.append('%d' %(temp % 10))
            right_1 -= 1
            right_2 -= 1
        return "".join(l[::-1])
            