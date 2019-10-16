class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        """
        Consider using Dfs:
        Step one:
        Add node value to array
        Then go to left and right nodes and do the same"""
        self.path = []
        self.master_path = []
        self.find_paths(root)
        for i in range(len(self.master_path)):
            p = self.changeformat(self.master_path[i])
            self.master_path[i] = p
        return self.master_path
    def find_paths(self, node):
        if node is None:
            return
        self.path.append(node.val)
        if node.left is None and not node.right:
            self.master_path.append(tuple(self.path))

        self.find_paths(node.left)
        self.find_paths(node.right)
        self.path.pop()

    def changeformat(self, array):
        new = '' + str(array[0])
        for i in range(1,len(array)):
            new = new + "->" + str(array[i])
        return new   
