class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #put data in graph
        
        visited = [False] * numCourses
        onStack = [False] * numCourses
        
        self.hasCycle = False
        graph = collections.defaultdict(list)
        for group in prerequisites:
            graph[group[1]].append(group[0])
        
        def dfs(graph, v):
            
            visited[v] = True
            onStack[v] = True
            for w in graph[v]:
                if self.hasCycle: return
                
                elif not visited[w]: dfs(graph, w)
                
                elif onStack[w]: self.hasCycle = True
                    
            onStack[v] = False
            
        
        def isValidSchedule():
            return not self.hasCycle
        
        
        for i in list(graph):
            if not visited[i]: dfs(graph,i)
        
        return True if not self.hasCycle else False
