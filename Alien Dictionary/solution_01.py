class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        words_len = len(words)
        if words_len == 0:
            return True
        alien_dic = {}
        for i in range(len(order)):
            alien_dic[order[i]] = i
        first_word = words[0]
        for word_index in range(1,words_len):
            if len(first_word) > len(words[word_index]):
                limit = len(words[word_index])
            else:
                limit = len(first_word)
            for char in range(len(first_word)):
                if char > limit - 1:
                    print(len(words[word_index]))
                    return False
                elif (alien_dic[first_word[char]] < alien_dic[words[word_index][char]]):
                    break
                elif(alien_dic[first_word[char]] == alien_dic[words[word_index][char]]):
                    continue
                else:
                    return False
            first_word = words[word_index]
        return True
