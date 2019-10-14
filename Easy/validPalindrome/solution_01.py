class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub('[^0-9a-zA-Z]', '', s).lower()
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i, j = i + 1, j - 1
        # empty or palindrome return True
        return True
   
        
