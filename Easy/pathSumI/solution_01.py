class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """dealing with recursive functions:
        do not forget base case
        keep in mind the field to be returned, 
        python is dynamic so it can be really deceiving"""
        if root is None:
            return False
        
        #root has passed, now we reduce the sum value
        sum -= root.val
        #check if we are at a leaf
        if not root.left and not root.right:
            return sum == 0
        
        #if we're not at leaf, recursively repeat the process
        #until we arrive at the leaf
        
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
