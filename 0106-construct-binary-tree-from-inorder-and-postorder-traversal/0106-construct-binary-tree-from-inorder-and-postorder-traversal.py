# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        root = TreeNode(postorder[-1])
        
        sep_idx = inorder.index(postorder[-1])
        
        in_left = inorder[:sep_idx]
        in_right = inorder[sep_idx+1:]
        
        post_left = postorder[:len(in_left)]
        post_right = postorder[len(in_left):len(postorder)-1]
        
        root.left = self.buildTree(in_left, post_left)
        root.right = self.buildTree(in_right, post_right)
        return root