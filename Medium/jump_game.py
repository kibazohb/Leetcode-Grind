class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        N = len(nums)
        max_jump = 0
        
        for i in range(N):
            if max_jump < i:
                return False
            max_jump = max(max_jump, i + nums[i])
            

        return True 
