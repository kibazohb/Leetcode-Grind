from collections import defaultdict
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float("-inf")
        self.max_gain(root)
        return self.max_sum
    def max_gain(self,node):
        if not node:
            return 0
        
        #get maximum gain from all nodes on left and right side
        #we will rather add zero that a negative number.
        left_gain = max(self.max_gain(node.left),0)
        right_gain = max(self.max_gain(node.right),0)
        
        self.max_sum = max(self.max_sum, left_gain + right_gain + node.val)
        
        #path with greater sum is below 
        return node.val + max(left_gain,right_gain)
