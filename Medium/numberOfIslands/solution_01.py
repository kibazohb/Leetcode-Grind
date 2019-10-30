class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        self.x = len(grid)
        self.y = len(grid[0])
        self.grid = grid
        num_of_islands = 0   
        
        
        for i in range(self.x):
            for j in range(self.y):
                if self.grid[i][j] == "1":
                    num_of_islands+=1
                    self.dfs(i,j)
                               
        return num_of_islands            
                
    def dfs(self, x,y):
        if self.is_valid(x,y) and self.grid[x][y] == "1":
            
            self.grid[x][y] = "0"
            self.dfs(x-1,y)
            self.dfs(x+1,y)
            self.dfs(x,y-1)
            self.dfs(x,y+1)
            
            
        else:
            return
        
        
    
    
    def is_valid(self,x,y):
        return 0 <= x < self.x and 0 <= y < self.y
