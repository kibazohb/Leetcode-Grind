class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(candidates, target, res, path,start):
            
            if target == 0:
                res.append(path[:])
                return 
                
            for i in range(start,len(candidates)):
                
                if candidates[i] > target:
                    return
                
                path.append(candidates[i])
                
                dfs(candidates, target - candidates[i], res, path,i)
                path.pop()
            
        res = []
        dfs(sorted(candidates), target, res, [], 0)
        return res
        
        
