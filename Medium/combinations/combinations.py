class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def dfs(res,path,start,nums,k):
            
            if len(path) == k:
                res.append(path[:])
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                
                dfs(res, path, i+1, nums,k)
                path.pop()
            return res
        
        return dfs([], [], 0, [x for x in range(1,n+1)], k)
