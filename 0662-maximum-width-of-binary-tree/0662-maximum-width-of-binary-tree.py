# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root, 0))
        res = 0
        
        while q:
            start = 0
            end = 0
            level = len(q)
            for i in range(level):
                node, col = q.popleft()
                if i == 0:
                    start = col
                if i == level - 1:
                    end = col
                if node.left:
                    q.append((node.left, 2*col))
                if node.right:
                    q.append((node.right, 2*col+1))
            res = max(res, end-start+1)
            print(res)
        return res
                
            
        