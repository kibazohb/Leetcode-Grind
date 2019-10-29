import numpy as np
class Solution:
    def updateMatrix(self, matrix):
        self.x = len(matrix)
        self.y = len(matrix[0])
        self.out = -1 * np.ones_like(matrix)
        for x in range(self.x):
            for y in range(self.y):
                if matrix[x][y] == 0:
                    self.out[x][y] = 0
                   
        for x1 in range(self.x):
            for y1 in range(self.y):
                if self.out[x1][y1] < 0:
                    self.dfs(x1,y1)            
        return self.out            
    def dfs(self,x,y):
        if not self.inbounds(x,y) and :
            return 0
        if self.out[x][y] == 0:
            return 0
        
        temp = 1 + min(self.dfs(x-1,y), self.dfs(x+1,y), self.dfs(x,y-1), self.dfs(x,y+1))
        self.out[x][y] = temp
        #print(temp,x,y)
        return temp
        
    def inbounds(self,x,y):
        return 0 <= x < self.x and 0 <= y < self.y  

