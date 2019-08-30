class Solution:
    def minSteps(self, n: int) -> int:
        
        #prime factorization technique
        ans = 0
        for i in range(2,n+1):
            while n % i == 0: #repeatedly divide till the prime factor is exhausted
                n = n//i
                ans += i
                
        
            
        return ans       
        
