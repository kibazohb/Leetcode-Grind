class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        """for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and j - i <= k:
                    return True
        return False"""
        h = {}
        for i in range(len(nums)):
            if nums[i] not in h:
                h[nums[i]] = i
            elif i - h[nums[i]] <= k:
                return True
            else:
                h[nums[i]] = i
        return False 
