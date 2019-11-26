class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if not root:
            return ""
        self.res=chr(10000)
        subpath = []
        self.getPaths(root, subpath)
        return self.res  
            
        
    def getPaths(self,node, subpath):
        if not node:
            return 
        subpath.append(chr(node.val + ord('a')))              
        if not node.left and not node.right:
            self.res = min(self.res, ''.join(reversed(subpath)))
            
        self.getPaths(node.left, subpath) 
        self.getPaths(node.right, subpath)
        subpath.pop()
