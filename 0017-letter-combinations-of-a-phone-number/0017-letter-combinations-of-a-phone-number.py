class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        def backtrack(d, path, res):
            if len(path) == len(digits):
                res.append("".join(path[:]))
                return
            for ch in hashmap[d[0]]:
                path.append(ch)
                backtrack(d[1:], path, res)
                path.pop()
              
        if not digits:
            return []
        res = []
        backtrack(digits, [], res)
        
        return res
        