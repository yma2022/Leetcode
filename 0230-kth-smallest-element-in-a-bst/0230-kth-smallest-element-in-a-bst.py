# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root, result):
            if not root:
                return
            inorder(root.left, result)
            result.append(root.val)
            inorder(root.right, result)
        res = []
        inorder(root, res)
        print(res)
        return res[k-1]
        