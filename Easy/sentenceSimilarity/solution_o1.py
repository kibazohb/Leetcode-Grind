class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        """#base case
        if len(words1) != len(words2):
            return False
        elif len(pairs) == 0:
            return True
        
        def putwords(pair):
            similarWords = {}
            for item in pair:
                similarWords[item[0]] = item[1]
                similarWords[item[1]] = item[0]    
                
            return similarWords 
        pairDict = putwords(pairs)
        #go through both sentences and check if each word is a pair.
        
        i = 0
        while i < len(words1):
            if pairDict[words1[i]] != words2[i]:
                return False
            i+=1
        return True"""  
        from collections import defaultdict
        if len(words1) != len(words2):
            return False
        
        pairDict = defaultdict(set)
        
        for pair in pairs:
            pairDict[pair[0]].add(pair[1])
            pairDict[pair[1]].add(pair[0])
            
        i = 0
        print(pairDict)
        while i < len(words1):
            if words1[i] == words2[i] or words1[i] in pairDict[words2[i]] or words2[i] in pairDict[words1[i]]:
                i+=1
                continue
            
            return False
        return True
