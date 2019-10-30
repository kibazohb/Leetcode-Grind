from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.graph = defaultdict(set)
        self.visited = [True]*n
        self.count = 0
        for u,v in edges:
            self.graph[u].add(v)
            self.graph[v].add(u)
        print(self.graph)      
        for i in range(n):
            if self.visited[i]:
                self.dfs(i)
                self.count+=1
        return self.count    
    def dfs(self, idx):
        if self.visited[idx]:
            self.visited[idx] = False
            for node in self.graph[idx]:
                self.dfs(node)
        return   
