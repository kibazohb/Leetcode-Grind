class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        final = []
        
        #first loop iterates from first item to second third last item
        temp_min = float('inf')
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start, end = i + 1, len(nums) - 1
            
            while start < end: 
                total = nums[i] + nums[start] + nums[end]
                if abs(target - total) < abs(target - temp_min):
                    temp_min = total
                
                if total > target:
                    while start < end and nums[end] == nums[end - 1]:
                        end = end - 1
                    end-=1
                else:
                    if total == target:
                        return total
                    while start < end and nums[start] == nums[start + 1]:
                        start = start + 1
                    start+=1    
        return temp_min           
 
        
        """if len(nums) == 3:
            return sum(nums)
        mydict = {}
        k = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    k = abs(target - (nums[i] + nums[j]))
                    if k not in mydict:
                        mydict[k] = [nums[i], nums[j]]
                    elif nums[i] + nums[j] < mydict[k][0] + mydict[k][1]:
                        mydict[k] = [nums[i], nums[j]]
                        
        
        nums.sort()
        temp = float('inf')
        num = max(mydict, key=mydict.get)
        small = num
        for i in nums:
            if i != mydict[num][0] and i != mydict[num][1]:
                if abs(i - small) < abs(small - temp):
                    temp = i
        
        if temp == float('inf'):
            temp = nums[0] 
        
        return temp + mydict[num][0] + mydict[num][1]  
    """
    
        """"""
