# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, path, target, results):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right and target == node.val:
                results.append(path[:])
            else:
                dfs(node.left, path, target - node.val, results)
                dfs(node.right, path, target - node.val, results)
            path.pop()
            
        res = []
        dfs(root, [], targetSum, res)
        return res
            
        