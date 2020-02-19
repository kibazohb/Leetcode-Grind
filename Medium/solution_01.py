class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cache = {0:1, 'res': 0};
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if total-k in cache:
                cache['res'] += cache[total-k]
                
            if total not in cache:
                cache[total] = 1
            else:
                cache[total] += 1   
            
        return cache['res']    
