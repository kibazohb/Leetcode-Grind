class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        self.x = len(board)
        
        death = ["b", "p", "r"]
        block = ["B","P"]
        
        def find(board):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == 'R':
                        return (i,j)
                    
                    
        def kill(board, pos):
            up = pos[1] - 0
            down = self.x - pos[1]
            left = pos[0] - 0
            right = self.x - pos[0]
            
            kills = 0
            i,j =pos[0],pos[1]
            for k in range(1,up):
            
                if board[i][j - k] in death:
                    kills += 1
                    print(k)
                    break
                elif board[i][j-k] in block:
                    break    
                else:
                    continue
                   
            for k in range(1,down):
                if board[i][j+k] in death:
                    kills += 1
                    break
                elif board[i][j+k] in block:
                    break    
                else:
                    continue       
            for k in range(1,left):
                if board[i-k][j] in death:
                    kills += 1 
                    #print(k)
                    break
                elif board[i-k][j] in block:
                    break    
                else:
                   
                    continue  
            for k in range(1,right):
                if board[i+k][j] in death:
                    kills += 1
                    #print(k)
                    break
                    
                elif board[i+k][j] in block:
                    break
                else:
                    
                    continue
            return kills   
        posi = find(board)
        return kill(board,posi)
                    
                    
