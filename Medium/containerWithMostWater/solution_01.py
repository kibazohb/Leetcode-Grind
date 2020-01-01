class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height: return
        volume = 0
        i,j = 0,len(height)-1
        while i < j:
            volume = max(self.calc_volume(i,j,height),volume)
            
            if height[i] < height[j]: 
                i+=1;
            else:
                j-=1;
        return volume    
    
    def calc_volume(self, i,j,h) -> int:
        return min(h[i], h[j]) * (j - i)
