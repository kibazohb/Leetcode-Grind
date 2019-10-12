class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ");
        for i in range(len(words)):
            temp = self.reverse(words[i])
            words[i] = temp
        return " ".join(words)    
    
    def reverse(self, word):
        word = self.splitword(word)
        left,right = 0,len(word) - 1
        while left < right:
            word[left], word[right] = word[right], word[left]
            left+=1;right-=1
        return "".join(word)
    def splitword(self, element):
        store = []
        for i in element:
            store.append(i)
        return store 
