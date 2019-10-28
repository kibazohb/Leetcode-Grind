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
        
        def dfs(w1,w2, visited) -> bool:
            if w1 == w2:
                return True
            
            if w2 in graph:
                for neighbour in graph[w2]:
                    if (w1,neighbour) not in visited:
                        visited.add((w1,neighbour))
                        if dfs(w1,neighbour,visited):
                            print(visited)
                            return True
                        
                return False
            else:
                return False
            
        for word1,word2 in zip(words1,words2):
            if not dfs(word1, word2, visited = set()):
                
                return False
            
        return True
            
            
    
