class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.v = v
        self.row , self.col = 0,0

    def next(self) -> int:
        self.hasNext()
        num = self.v[self.row][self.col]
        self.col += 1
        return num
                

    def hasNext(self) -> bool:
        while self.row < len(self.v):
            if self.col < len(self.v[self.row]):
                
                return True
            
            self.col = 0
            self.row += 1
        return False
