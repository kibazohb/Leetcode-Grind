class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        out = []
        self.traverse(root,out)
        return out[k-1]
        
    def traverse(self,node,arr):
        if not node:
            return None
        #inorder because it puts the array in increasing order
        self.traverse(node.left,arr)
        arr.append(node.val)
        self.traverse(node.right,arr)
        
        """The overall timecomplexity is O(N+k) time. 
        TIme to traverse the entire BST and then traverse the array for 
        the kth elemeent
        
        Space complexity: O(N), since we only store the elements of the array."""
