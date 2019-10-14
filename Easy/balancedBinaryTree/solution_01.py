class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        
        if abs(left - right) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def getHeight(self, node):
        if node is None:
            return 0
        
        return 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        
