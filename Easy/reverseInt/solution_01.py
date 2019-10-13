class Solution:
    def reverse(self, x: int) -> int:
        out = 0
        neg = False
        max_32 = 2**32 -1
        min_32 = -1*2**32 -1
        if x < 0:
            neg = True
            x = - 1 * x
        while x:
            lstnum = x % 10
            x = x // 10
            out = out*10 + lstnum
            
            #special test cases
            if (out > max_32//10) or (out == max_32//10 and lstnum >7):
                return 0
            if (out < min_32//10) or (out == min_32//10 and lstnum < -8):
                return 0
        
        if neg:
            return -1*out
        else:
            return out 
