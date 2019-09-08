def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
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
        
