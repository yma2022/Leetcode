# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        res=[root.val]
        def leftBoundary(root):
            if root is None or root.left is None and root.right is None: return
            res.append(root.val)
            if root.left:
                leftBoundary(root.left)
            else:
                leftBoundary(root.right)
            
        def rightBoundary(root):
            if root is None or root.left is None and root.right is None: return
            if root.right:
                rightBoundary(root.right)
            else:
                rightBoundary(root.left)
            res.append(root.val)
            
        def leaves(node):
            if node is None: return
            if node.left is None and node.right is None and node != root:
                res.append(node.val)
            leaves(node.left)
            leaves(node.right)
        
        leftBoundary(root.left)
        leaves(root)
        rightBoundary(root.right)
        return res