class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        #the middle is usually the root node
        #everything on the left of the middle node, is the left subtree
        #the rest is on the right subtree
        return self.splitTree(nums, 0, len(nums) - 1)
    
    
    def splitTree(self, array, left, right): 
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(array[mid])
        root.left = self.splitTree(array, left, mid - 1)
        root.right = self.splitTree(array, mid + 1, right)
        
        return root
