class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for element in s[ : : -1]:
            
            if result // d[element] == 5 or result // d[element] == 10:
                result -= d[element]
            else:
                result += d[element]
        return result
            
            