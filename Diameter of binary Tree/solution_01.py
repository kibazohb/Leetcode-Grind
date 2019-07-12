class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.count = 1
        self.getDepth(root)
        return self.count - 1
        
    def getDepth(self, node):
        if node is None:
            return 0
        left = self.getDepth(node.left)
        right = self.getDepth(node.right)
        
        self.count = max(self.count, left + right + 1)
        
        #getting the depth of the binary tree, used and called recursively
        return 1 + max(left,right)
