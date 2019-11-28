class Solution:
    def longestMountain(self, A: List[int]) -> int:
        res = 0
        i = 0
        while i < len(A):
            j = i
            if j + 1 < len(A) and A[j] < A[j+1]:
                while j + 1 < len(A) and A[j] < A[j+1]:
                    j+=1
                if j + 1 < len(A) and A[j] > A[j+1]:
                    while j + 1 < len(A) and A[j] > A[j+1]:
                        j+=1
                    res = max(res, j - i + 1)
            i = max(i+1,j)
        return res
