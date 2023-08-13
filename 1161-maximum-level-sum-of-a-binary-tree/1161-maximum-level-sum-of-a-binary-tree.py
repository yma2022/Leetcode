# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        level = 0
        max_sum = float('-inf')
        res = 0
        while q:
            length = len(q)
            level += 1
            total = 0
            for _ in range(length):
                node = q.popleft()
                total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if total > max_sum:
                max_sum = total
                res = level
        return res
            
        