# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            left = dfs(root.left)
            right = dfs(root.right)
            return max(left, right) + 1
        
        height = dfs(root)
        
        q = deque([root])
        res = 0
        while q:
            length = len(q)
            height -= 1
            for _ in range(length):
                node = q.popleft()
                if not height:
                    res += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
        return res
        