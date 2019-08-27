class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        self.arr = []
        self.traverse(root)
        
        return len(set(self.arr)) == 1
                
    def traverse(self,node):
        if node is None:
            return 0
        else:
            self.arr.append(node.val)
            self.traverse(node.left)
            self.traverse(node.right)
        return self.arr   
