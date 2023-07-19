class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []  # 存放结果集
        self.backtracking(k, n, 1, [], result)
        return result
        
    def backtracking(self, k, n, startIndex, path, result):
        if len(path) == k and sum(path) == n:
            result.append(path[:])
            return
        for i in range(startIndex, 10):  # 需要优化的地方
            path.append(i)  # 处理节点
            self.backtracking(k, n, i + 1, path, result)
            path.pop()  # 回溯，撤销处理的节点
            
        