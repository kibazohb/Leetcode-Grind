class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        #root->left->right
        #for iterative approach use stack
        out = []
        myStack = []
        myStack.append(root)
        while myStack:
            curr = myStack.pop()
            if curr:
                out.append(curr.val)
                myStack.append(curr.right)
                myStack.append(curr.left)        
        return out  
