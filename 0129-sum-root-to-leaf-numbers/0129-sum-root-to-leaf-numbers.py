# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, res):
            if not root:
                return None
            if not root.left and not root.right:
                arr.append(res+root.val)
                return
            dfs(root.left, (res+root.val)*10)
            dfs(root.right, (res+root.val)*10)
        
        if not root:
            return 0
        res = 0
        arr = []
        dfs(root, res)
        return sum(arr)
        