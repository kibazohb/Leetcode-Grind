from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        #groupsize -> number of people
        #IDs -> 0 to groupsize
        #groupsize -> key 
        res = []
        cache = defaultdict(list)
        for i in range(len(groupSizes)):
            cache[groupSizes[i]].append(i)
            if groupSizes[i] == len(cache[groupSizes[i]]):
                res.append(cache[groupSizes[i]])
                del cache[groupSizes[i]]       
        return res
