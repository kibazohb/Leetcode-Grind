from collections import defaultdict
class Solution:
    def expand(self, S: str) -> List[str]:
        """
        "{a,b}c{d,e}f"
        Questions to ask: Will sequence of characters be in order?
        can we have more than one interfering character?
        can we have interfering characters at the beginning of the string?
        
        DFS approach (i personally prefer this approach.)
        When we deal with recursiom, the return function pretty much helps to
        pop the current item off the stack, then it deals with the rest.
        """
        graph = defaultdict(list)
        access = False
        inside = []
        path = ''
        idx = 0
        self.out=[]
        for x in S:
            if x == "{":
                access = True
            elif x == ",":
                continue
            elif x == "}":
                access = False
                idx += 1 
            elif access:
                graph[idx].append(x)
            else:
                graph[idx].append(x)
                idx+=1  
        print(graph)        
        self.dfs(path,graph,0)
        return sorted(self.out)
                
    def dfs(self, path, graph, idx) -> None:
        if len(path) == len(graph):
            self.out.append(path)
            return None
            
        for char in graph[idx]:
            self.dfs(path + char, graph, idx + 1)
