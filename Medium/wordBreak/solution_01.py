from collections import deque;
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
 
        q = collections.deque()
        q.append(0)
        visited = [0 for i in range(len(s)+1)]
        while q:
            start = q.popleft()
            if not visited[start]:
                for i in range(start + 1, len(s)+1):
                    if s[start:i] in wordDict:
                        q.append(i)
                        if (i == len(s)):
                            return True
                visited[start] = 1        
                    
        return False
        
