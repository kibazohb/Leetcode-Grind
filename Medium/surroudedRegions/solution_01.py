class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #create visited array (a duplicate of the board)
        #use stack to keep track of 0's
        #solving the problem iteratively
        if not board: return None
        self.x = len(board)
        self.y = len(board[0])
        
        self.visited = [[1 if row[i] == "X" else 0 for i in range(self.y)] for row in board]
        for i in range(1,self.x):
            for j in range(1,self.y):
                if board[i][j] == "O":
                    self.path = []
                    self.board = board
                    self.redflag = False
                    self.dfs(i,j)
                    if self.redflag:
                        continue
                    else:
                        for pos in self.path:
                            board[pos[0]][pos[1]] = 'X'
    def dfs(self, i,j):
        if self.isbounded(i,j) and self.visited[i][j] == 0 and self.board[i][j] == "O": 
            self.visited[i][j] = 1
            if (i == 0 or i == self.x -1 or j == 0 or j == self.y -1): self.redflag = True               
            if (0 < i < (self.x) - 1 ) and (0 < j < self.y - 1 ): self.path.append((i,j))
                  
            self.dfs(i+1,j)
            self.dfs(i-1,j)
            self.dfs(i,j+1)
            self.dfs(i,j-1)
        else:
            return    
    def isbounded(self,i,j):
        return 0 <= i < self.x and 0 <= j < self.y
