class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        #number of rows
        rows = len(board)
        #number of columns
        col = len(board[0])
        
        #number of battleships
        ships = 0
        for i in range(rows):
            for j in range(col):
                if board[i][j] == "X":
                    #check the bottom and the right for adjacent X's
                    if i + 1 < rows and board[i+1][j] == "X" or j + 1 < col and board[i][j+1] == "X":
                        continue
                    ships += 1    
        return ships                
