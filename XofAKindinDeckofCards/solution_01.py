class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        deck_dic = {} 
        for x in deck:
            if x not in deck_dic:
                deck_dic[x] = 1
            else:
                deck_dic[x] = deck_dic[x] + 1        
        low = min(deck_dic.values())
        if low <= 1:
            return False
        for val in deck_dic.values():
            if (val % low != 1 ):
                partition = True
            else:
                partition = False
                break
        return partition
