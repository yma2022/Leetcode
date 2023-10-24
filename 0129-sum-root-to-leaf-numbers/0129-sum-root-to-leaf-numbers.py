# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            nonlocal result
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                result += int("".join(path[:]))
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        
        result = 0
        dfs(root, [])
        return result