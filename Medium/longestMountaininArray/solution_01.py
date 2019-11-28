class Solution:
    def longestMountain(self, A: List[int]) -> int:
        risen = False
        fell = False
        res = 0
        i,j = 0,1
        while j < len(A):
            if risen or fell:
                if A[j-1] > A[j]:
                    j+=1
                    fell = True
                    risen = False
                    res = max(res, j - i)
                elif A[j] > A[j-1]:
                    j+=1
                    fell = False
                else:
                    i = j
                    j+=1
                    risen , fell = False, False
            elif A[j] > A[j-1]:
                risen = True
                j+=1
            else:
                j+=1
                i+=1
                #risen , fell = False, False
        return res
