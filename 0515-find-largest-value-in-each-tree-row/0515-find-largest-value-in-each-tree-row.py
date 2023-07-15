# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        
        q = deque()
        res = []
        q.append(root)
        
        while q:
            maxVal = float('-inf')
            for _ in range(len(q)):
                curr = q.popleft()
                maxVal = max(curr.val, maxVal)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(maxVal)
        return res
        