class Solution:
    def findTilt(self, root: TreeNode) -> int:
        
        self.tilt = 0 #create state variable, simplifies final process
        self.traverse(root)
        return self.tilt
        
    def traverse(self, node):
        if node is None:
            return 0
        sum_left, sum_right = 0,0
        ##traverse down the subtree performing the and getting the tilt sum on each root
        if node.left is not None:
            sum_left = self.traverse(node.left)
        if node.right is not None:
            sum_right = self.traverse(node.right)  
        
        self.tilt += abs(sum_left - sum_right)
        
        #recursively return the sum of the subtree
        return node.val + sum_left + sum_right
