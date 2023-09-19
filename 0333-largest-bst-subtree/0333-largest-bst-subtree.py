# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def isValidBST(root):
            nonlocal prev
            if not root:
                return True
            if not isValidBST(root.left):
                return False
            if prev and prev.val >= root.val:
                return False
            prev = root
            return isValidBST(root.right)
        
        def countNodes(root):
            if not root:
                return 0
            return 1 + countNodes(root.left) + countNodes(root.right)
        
        if not root:
            return 0
        prev = None
        
        if isValidBST(root):
            return countNodes(root)
        
        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))
        