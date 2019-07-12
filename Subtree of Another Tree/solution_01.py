class Solution:
    
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if self.check(s,t):
            return True
        if s is None:
            return False
        else:
            return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
        
    def check(self,s,t):    
        if s is None and t is None:
            return True
        elif s is not None and t is not None:
            return (s.val == t.val) and self.check(s.left,t.left) and self.check(s.right,t.right)
        else:
            return False
