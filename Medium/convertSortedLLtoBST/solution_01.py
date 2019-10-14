class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        return self.buildTree(head)
    
    def buildTree(self, node):
        if node is None:
            return None
        # we find the middle node
        slow = fast = node
        slower = None
        while fast and fast.next:
            fast = fast.next.next
            slower = slow
            slow = slow.next
        
        #break left-side from the list.
        if slower:
            slower.next = None
        
        root = TreeNode(slow.val)
        if slow == node:
            return root
        root.left = self.buildTree(node)
        root.right = self.buildTree(slow.next)
        
        return root
