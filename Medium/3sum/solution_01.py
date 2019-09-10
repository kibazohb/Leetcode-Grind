class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """nums = sorted(nums)
        final =  []
        for i in range(len(nums) - 3):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            start = i + 1
            end = len(nums) - 1
            while start < end:
                if nums[i] + nums[start] + nums[end] == 0:
                    final.append([nums[i], nums[start], nums[end]])
                    while start < end and nums[start] == nums[start + 1]:
                        start+=1
                    while start < end and nums[end] == nums[end-1]:
                        end-=1
                    start+=1
                    end+=1




                elif nums[i] + nums[start] + nums[end] < 0:
                    start+=1

                elif nums[i] + nums[start] + nums[end]:
                    end-=1

                
        return final """
        res = []
        nums.sort()
        length = len(nums)
        for i in range(length-2): #[8]
            if nums[i]>0: break #[7]
            if i>0 and nums[i]==nums[i-1]: continue #[1]

            l, r = i+1, length-1 #[2]
            while l<r:
                total = nums[i]+nums[l]+nums[r]

                if total<0: #[3]
                    l+=1
                elif total>0: #[4]
                    r-=1
                else: #[5]
                    res.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l]==nums[l+1]: #[6]
                        l+=1
                    while l<r and nums[r]==nums[r-1]: #[6]
                        r-=1
                    l+=1
                    r-=1
        return res      
        

