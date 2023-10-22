# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:        
        def allPossibleBST(start, end, memo):
            res = []
            if start > end:
                res.append(None)
                return res
            if (start, end) in memo:
                return memo[(start, end)]
            
            for i in range(start, end+1):
                leftSub = allPossibleBST(start, i-1, memo)
                rightSub = allPossibleBST(i+1, end, memo)
                
                for l in leftSub:
                    for r in rightSub:
                        root = TreeNode(i, l, r)
                        res.append(root)
            memo[(start, end)] = res
            return res
        memo = {}
        return allPossibleBST(1, n, memo)
        