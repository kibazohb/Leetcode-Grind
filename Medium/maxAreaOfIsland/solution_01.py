class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.x = len(grid)
        self.y = len(grid[0])
        self.dummy = grid
        res = 0
        for i in range(self.x):
            for j in range(self.y):
                if self.dummy[i][j] == 1:
                    self.count = 0
                    self.dfs(i,j)
                    res = max(res, self.count)
        return res           
    def dfs(self, i,j):
        if self.isSafe(i,j) and self.dummy[i][j] == 1:
            self.count+=1
            self.dummy[i][j] = 0
            self.dfs(i+1, j)
            self.dfs(i-1,j)
            self.dfs(i,j+1)
            self.dfs(i,j-1)
            
        else:
            return
    def isSafe(self,x,y):
        return 0 <= x < self.x and 0 <= y < self.y
