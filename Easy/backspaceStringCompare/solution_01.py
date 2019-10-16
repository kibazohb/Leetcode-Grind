class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        #stack method
        
        return self.build(S) == self.build(T)
    
    def build(self, K):
        res = []
        for i in K:
            if i != "#":
                res.append(i)
            elif res:
                res.pop()
        return res  
