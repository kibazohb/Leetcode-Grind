class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        p = len(nums)
        a =0
        b = a + 1
        c = b + 1
        mint = float("inf") 
        
        for i in range(a, p):
            for j in range(b,p):
                for k in range(c,p):
                    if i != j and j !=k and i != k:
                    
                        temp = nums[i] + nums[j] + nums[k]
                        if temp == target:
                            return nums[i] + nums[j] + nums[k]
                        if abs(target - temp) < abs(mint - target):
                            mint = temp
                    
                       
      
        return mint
