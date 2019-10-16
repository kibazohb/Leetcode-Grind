
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        #add all secret values onto dictionary
        s_dic = {}
        for c in secret:
            if c not in s_dic:
                s_dic[c] = 1
            else:
                s_dic[c]+=1  
          
        A,B=0,0        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A+=1
                #deduct to avoid conflict with next loop
                s_dic[secret[i]] -= 1
                
        for i in range(len(secret)):
            if secret[i] != guess[i] and guess[i] in secret and s_dic[guess[i]] > 0:
                s_dic[guess[i]] -= 1
                
                B+=1
        return str(A)+"A"+str(B)+"B"        
        
                
                
        
