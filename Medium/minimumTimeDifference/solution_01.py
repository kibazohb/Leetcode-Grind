class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        times = [self.convert_to_int(i) for i in timePoints]
        times.sort()
        #the least time would happen over night
        end = 24*60
        minimum_time = end - int(times[-1]) + int(times[0])
        
        for i in range(1,len(times)):
            minimum_time = min(minimum_time, times[i] - times[i-1])
        return minimum_time    
    def convert_to_int(self, time):
        h,m=time.split(":")
        return int(h)*60 + int(m)
