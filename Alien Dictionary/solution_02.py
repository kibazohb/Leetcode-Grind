class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_dic = {c:i for i, c in enumerate(order)}
        for a,b in zip(words, words[1:]):
            if len(a) > len(b) and a[:len(b)] == b:
                return False
            for s1,s2 in zip(a,b):
                if alien_dic[s1] < alien_dic[s2]:
                    break
                elif alien_dic[s1] > alien_dic[s2]:
                    return False
        return True
