class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        myStack = []
        out = []
        curr = root
        
        while True:
            
            if curr != None:
                myStack.append(curr)
                curr = curr.left
            elif myStack:
                curr = myStack.pop()
                out.append(curr.val)
                curr = curr.right
            else:
                break    
        return out    
