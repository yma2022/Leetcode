# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:

        q = deque([root])
        res = []
        
        while q:
            length = len(q)
            for _ in range(length):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    if not node.right:
                        res.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    if not node.left:
                        res.append(node.right.val)
                        
        return res
        