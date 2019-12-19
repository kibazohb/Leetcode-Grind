class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return 
        self.preorder = preorder
        self.inorder = inorder
        idx = {inorder[i]:i for i in range(len(inorder))}
        parents = []
        i = 0
        root = TreeNode(preorder[i])
        parents.append(root)
        i+=1
        while i < len(preorder):
            refer = parents[-1]
            if idx[preorder[i]] < idx[refer.val]:
                newNode = TreeNode(preorder[i])
                refer.left = newNode
                parents.append(newNode)
                i+=1
            else:
                while idx[refer.val] < idx[preorder[i]] and parents:
                    hold = parents[-1]
                    parents.pop()
                    if parents: refer = parents[-1] 
                    
                newNode = TreeNode(preorder[i])
                hold.right = newNode
                parents.append(newNode)
                i+=1
        return root
