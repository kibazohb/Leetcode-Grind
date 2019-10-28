from collections import defaultdict
class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        #base cases
        if len(words1) != len(words2):
            return False
        if len(pairs) == 0 and words1 == words2:
            return True
        #put components in adjacent list
        graph = defaultdict(set)
        for pair in pairs:
            graph[pair[0]].add(pair[1])
            graph[pair[1]].add(pair[0])
        
        for w1,w2 in zip(words1,words2):
            stack = [w1]
            visited = {w1}
            while stack:
                word = stack.pop() 
                if word == w2:
                    break
                for nei in graph[word]:
                    if nei not in visited:
                        visited.add(nei)
                        stack.append(nei)
            else:
                return False
            
        return True  
