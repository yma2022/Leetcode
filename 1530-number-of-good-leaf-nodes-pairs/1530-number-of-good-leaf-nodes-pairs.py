# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.pairs = 0
        def dfs(node, dist):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            
            l_leaf_dists = dfs(node.left, dist)
            r_leaf_dists = dfs(node.right, dist)
            
            for l_dist in l_leaf_dists:
                if l_dist >= dist:
                    continue
                for r_dist in r_leaf_dists:
                    self.pairs += 1 if l_dist + r_dist <= dist else 0
            return [1 + dist for dist in l_leaf_dists + r_leaf_dists]
        
        if not root:
             return 0
        dfs(root, distance)
        return self.pairs
            