# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        
        sep_idx = inorder.index(preorder[0])
        
        in_left = inorder[:sep_idx]
        in_right = inorder[sep_idx+1:]
        
        pre_left = preorder[1:len(in_left)+1]
        pre_right = preorder[len(in_left)+1:]
        
        root.left = self.buildTree(pre_left, in_left)
        root.right = self.buildTree(pre_right, in_right)
        
        return root
        
        