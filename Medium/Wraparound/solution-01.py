class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        
        if p:
            dp = [0] * 26
            dp[ord(p[0]) - ord("a")] = 1
        else:
            return 0
        
        running_length = 1
        
        for i in range(1, len(p)):
            
            if (ord(p[i]) - ord(p[i-1])) % 26 == 1:
                running_length += 1
            else:
                running_length = 1

            dp[ord(p[i]) - ord("a")] = max(dp[ord(p[i]) - ord("a")], running_length)
            
            
        return sum(dp)
