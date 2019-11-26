class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if not root:
            return ""
        self.paths = []
        subpath = []
        self.getPaths(root, subpath)
        self.paths.sort(key = lambda x:(x[-1], len(x)))
        print(self.paths)
        return self.convertTostring(self.paths[0])
        #take first tuple and convert it to string of character
    def convertTostring(self,tup):
        res = ''
        for i in range(len(tup)-1,-1,-1):
            res += chr(tup[i] + 97)
        return res    
            
        
    def getPaths(self,node, subpath):
        if not node:
            return 
        subpath.append(node.val)
        if not node.left and not node.right:
            self.paths.append(tuple(subpath))
            
        self.getPaths(node.left, subpath) 
        self.getPaths(node.right, subpath)
        subpath.pop()
