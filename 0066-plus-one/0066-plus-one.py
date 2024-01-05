class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 0
        
        for i in range(len(digits)-1, -1, -1):
            sum = digits[i] + 1 + carry if i == len(digits)-1 else digits[i] + carry
            carry = sum // 10
            digits[i] = sum % 10
            
        return [carry] + digits if carry else digits