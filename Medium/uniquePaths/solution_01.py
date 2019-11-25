class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        self.x,self.y = m,n
        self.res = 0
        self.grid = [[-1]*n for _ in range(m)]   
        self.grid[m-1][n-1] = 1
        self.dfs(0,0)  
        return self.res
    def dfs(self, i, j):
        if not self.isValid(i,j):
            return
        if self.grid[i][j] == 1:
            self.res += 1
            return
        self.dfs(i+1,j)
        self.dfs(i,j+1)
    
    def isValid(self, x,y):
        return 0 <= x < self.x and 0 <= y < self.y  
