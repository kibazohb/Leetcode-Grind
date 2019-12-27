from collections import defaultdict
class Solution:
    """Runtime
       O(NM * log M)
       M is the length of the word
       N is the number of words in the input array
       Space O(NM)
       worst case scenario, no anagrams exist
       N is the number of words in the string,
       each word is an anagram of itself, with K number of characters"""
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = defaultdict(list)
        for i in range (len(strs)):
            cache[tuple(sorted(strs[i]))].append(strs[i])                    
        return [value for value in cache.values()] 
