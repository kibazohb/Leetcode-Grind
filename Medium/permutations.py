class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        mutation = []
        def dfs(path, numbers):
            if len(path) == len(nums):
                res.append(path[:])
                return 
            for num in (numbers):
                path.append(num)
                numbers = [x for x in nums if x not in path]
                dfs(path, numbers)
                path.pop()
        
        dfs(path,nums)
        return res
