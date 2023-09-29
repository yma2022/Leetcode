class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = (digits[-1] + 1) // 10
        digits[-1] = (digits[-1] + 1) % 10
        for i in range(n-2, -1, -1):
            # print(carry)
            digit_sum = (digits[i] + carry) % 10
            carry = (digits[i] + carry) // 10
            digits[i] = digit_sum
            
            
            
        if carry != 0:
            res = [carry]
            res.extend(digits)
            digits = res
        return digits
        