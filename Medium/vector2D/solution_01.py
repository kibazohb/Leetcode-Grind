class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.v = v
        self.vector_1D = []
        for i in range(len(self.v)):
            for j in range(len(self.v[i])):
                self.vector_1D.append(self.v[i][j])
        self.index = 0
        self.wall = len(self.vector_1D)

    def next(self) -> int:
        num = self.vector_1D[self.index]
        self.index +=1
        return num
            
            

    def hasNext(self) -> bool:
         return self.index < self.wall 
