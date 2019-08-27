class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        p_dic = {}
        final = []
        for string in B:
            for letter in string:
                if letter not in p_dic:
                    p_dic[letter] = 1
                else:
                    p_dic[letter] = max(p_dic[letter], string.count(letter))
        for word in A: 
            check = 0
            for key in p_dic.keys(): 
                j = word.count(key)
                if j < p_dic[key] or j == 0:
                    check +=1
                    break
                    
            if check == 0: final.append(word)    
                    
        return final 
