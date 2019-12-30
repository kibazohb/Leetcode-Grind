class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        self.res = [-1,""]
        self.s = s
        self.cache = collections.defaultdict(list)
        for i in range(len(s)):
            self.cache[s[i]].append(i)
            
        for key in self.cache.keys():
            self.find_palindrome(key)    
        return self.res[1]
    
    def find_palindrome(self, key) -> None:
        for i in range(len(self.cache[key])):
            for j in range(len(self.cache[key])-1, -1, -1):
                if not self.max_substring(key, i, j):
                    break
                
                if self.is_palindrome(self.cache[key][i], self.cache[key][j]):
                    self.res[0] = self.cache[key][j] - self.cache[key][i]
                    self.res[1] = self.s[self.cache[key][i]: self.cache[key][j]+1]
                    break 
                
                  
    def max_substring(self,key,i,j) -> bool:
        return (self.cache[key][j] - self.cache[key][i]) > self.res[0]
    
    def is_palindrome(self,i,j) -> bool:
        l,r = i,j
        while l < r:
            if self.s[l] == self.s[r]:
                l+=1
                r-=1
            else:
                return False
        return True
