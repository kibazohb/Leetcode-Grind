class Solution:
    
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        s_array = []
        t_array = []
        self.arrayseeker(s,s_array)
        self.arrayseeker(t,t_array)
        print(t_array)
        print(s_array)
        return "".join(t_array) in "".join(s_array)
        
    def arrayseeker(self,z,arr):
        if z is None:
            arr.append('#')
        else:
            #arr.append("\(%s\)"%(root.val))
            arr.append("\(%s\)"%(z.val))
            self.arrayseeker(z.left,arr)
            self.arrayseeker(z.right,arr)
