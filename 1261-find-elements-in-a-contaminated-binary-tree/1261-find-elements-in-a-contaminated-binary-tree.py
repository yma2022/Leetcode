# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        q = deque([root])
        self.val = []
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                self.val.append(node.val)
                if node.left:
                    node.left.val = 2 * node.val + 1
                    q.append(node.left)
                if node.right:
                    node.right.val = 2 * node.val + 2
                    q.append(node.right)
        self.root = root        

    def find(self, target: int) -> bool:
        return target in self.val
        
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)