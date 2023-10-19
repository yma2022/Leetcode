class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(leftRemain, rightRemain, path, results):
            if leftRemain > rightRemain or leftRemain < 0 or rightRemain < 0:
                return
            if leftRemain == 0 and rightRemain == 0:
                results.append(path[:])
                return
            dfs(leftRemain-1, rightRemain, path+"(", results)
            dfs(leftRemain, rightRemain-1, path+")", results)
        res = []
        dfs(n, n, "", res)
        return res
