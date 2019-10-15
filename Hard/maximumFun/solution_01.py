

"""given a grid / graph like below, find the maximum fun.
everytime to you move from a higher slope to lower,
we increase fun by 1. Given a specific point on a graph,
find the maximum fun."""

"""ski_resort = SkiResort(
    [[1, 2, 3, 4, 5],
     [16, 17, 18, 19, 6],
     [15, 24, 25, 20, 7],
     [14, 23, 22, 21, 8],
     [13, 12, 11, 10, 9]]
)
The result here would be 24"""


#approach to solve this question is dfs
#maximum height at 25 -> max(dfs(24), dfs(18), dfs(22), dfs(20))
import numpy as np
class Resort():
    def __init__(self, resort):
        self.resort = resort
        self.row = len(resort)
        self.col = len(resort[0])
        self.fun_grid = -1 * np.ones_like(resort)

    #function to detect the boundaries
    def is_safe(self,x,y):
        return 0 <= x < self.col and 0 <= y < self.row

    def calc_fun(self,i,j,last_height = float("int")):
        if not self.is_safe(i,j):
            return -1
        current_height = self.resort[i][j]
        if last_height <= current_height:
            return -1
        if self.resort[i][j] >= 0:
            return -1
        fun = 1 + max(self.calc_fun(i+1,j,current_height),
                    self.calc_fun(i-1,j,current_height)
                    self.calc_fun(i,j+1,current_height)
                    self.calc_fun(i,j-1,current_height))

        self.fun_grid[i][j] = fun
        return fun
