# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        def dfs(root, res):
            if not root:
                return
            dfs(root.left, res)
            res.append(root.val)
            dfs(root.right,res)
            return res
        
        arr = dfs(root, [])
        root = TreeNode(arr[0])
        curr = root
        for i in range(1, len(arr)):
            curr.right = TreeNode(arr[i])
            curr = curr.right
        return root
            
        