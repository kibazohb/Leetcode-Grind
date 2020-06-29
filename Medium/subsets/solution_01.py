from collections import defaultdict
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums, idx, path):
            if idx == len(nums)+1:
                return
            
            res.append(path)
            for i in range(idx, len(nums)):
                dfs(nums, i + 1, path + [nums[i]])
                
        
        dfs(nums, 0, [])
        return res
    
  
    
    
