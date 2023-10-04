class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        def backtrack(digits, comb, results):
            if len(comb) == n:
                results.append("".join(comb))
                return
            for c in d[digits[0]]:
                comb.append(c)
                backtrack(digits[1:], comb, results)
                comb.pop()
        if not digits:
            return []
        results = []
        n = len(digits)
        backtrack(digits, [], results)
        return results
                