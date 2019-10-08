class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftside = self.getHeight(root.left)
        rightside = self.getHeight(root.right)
        lefttree = self.diameterOfBinaryTree(root.left)
        righttree = self.diameterOfBinaryTree(root.right)
        
        return max((leftside + rightside ), max(lefttree,righttree))
        
        
    def getHeight(self,node):
        if node is None:
            return 0
        lefty,righty = self.getHeight(node.left), self.getHeight(node.right)
        return 1 + max(lefty,righty)
