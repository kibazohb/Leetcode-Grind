class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        """
        questions involving paths, always involve
        traversals, Its pretty much up to you to
        figure out which traversal is suitable to
        solve the problem.
        In this case, it is pre-order. (dfs)"""
        self.out = []
        self.myStack = []
        self.traverse(root, sum)
        return self.out
    def traverse(self, node, total):

        if not node:
            return

        self.myStack.append(node.val)
        total = total - node.val
        if not node.left and not node.right and total == 0:
            self.out.append(tuple(self.myStack))
        self.traverse(node.left, total)
        self.traverse(node.right,total)
        total = total + node.val
        self.myStack.pop()
