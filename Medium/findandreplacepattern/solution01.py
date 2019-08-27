class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        p_dic = {}
        tlist = []
        j = len(pattern)
        for i in range(j):
            if pattern[i] not in p_dic:
                p_dic[i] = pattern.index(pattern[i])
        print(p_dic)        
        for word in words:
            w_dic = {}
            k = len(word)
            for i in range(k):
                if word[i] not in w_dic:
                    w_dic[i] = word.index(word[i])
            print(w_dic)
            if w_dic == p_dic:
                tlist.append(word)
                
        return tlist
