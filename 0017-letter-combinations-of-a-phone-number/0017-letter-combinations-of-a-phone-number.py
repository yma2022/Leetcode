class Solution:
    def __init__(self):
        self.mapping = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        self.backtracking(digits, 0, "", result)
        return result
        
    def backtracking(self, digits, index, string, result):
        if len(string) == len(digits):
            result.append(string)
            return
        digit = int(digits[index])
        letters = self.mapping[digit]
        for i in range(len(letters)):
            string += letters[i]
            self.backtracking(digits, index+1, string, result)
            string = string[:-1]
        