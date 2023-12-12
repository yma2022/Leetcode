class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(left, right, path, res):
            if left > right or left < 0 or right < 0:
                return
            if left == 0 and right == 0:
                res.append(path)
                return
            
            backtrack(left-1, right, path+'(', res)
            backtrack(left, right-1, path+')', res)
            
        res = []
        backtrack(n, n, "", res)
        return res
        