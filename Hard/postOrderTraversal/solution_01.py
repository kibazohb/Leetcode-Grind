class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        initStack = []
        finalStack = []
        """
        postorder left -> right -> root
        store in stack in reverse
        we do not revisit a node
         
                        5
                     /      \
                    3.       7
                   / \        \
                  1.  6.       9  
        result -> 1,6,3,9,7,5"""
        
        initStack.append(root)
        while initStack:
            curr = initStack.pop()
            if curr:
                initStack.append(curr.left)
                initStack.append(curr.right)
                finalStack.append(curr.val)
        return finalStack[::-1]
