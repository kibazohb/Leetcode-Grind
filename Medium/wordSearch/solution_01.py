class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        if not word: 
            return True
      
        self.cols = len(board[0])
        self.rows = len(board)
        self.board = board
        self.word = word
        
        for i in range(self.rows):
            for j in range(self.cols):
                if self.dfs(i, j, 0):
                    return True
        return False
                
    def dfs(self, x,y,num) -> bool: 
        
        if not self.isValid(x,y): 
            return False
        
        if self.word[num] != self.board[x][y] or self.board[x][y] == '#':
            return False
        
        if num == len(self.word) - 1: 
            return True
        
        letter = self.board[x][y]
        self.board[x][y] = '#'
        
        
        if self.dfs(x+1,y, num + 1) or self.dfs(x-1,y, num + 1) or self.dfs(x,y+1, num + 1) or self.dfs(x,y-1, num + 1):
            return True
        
        self.board[x][y] = letter
        return False
        
        
    def isValid(self, x,y):
        return  0 <= x < self.rows and 0 <= y < self.cols
