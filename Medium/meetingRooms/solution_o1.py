class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        stime = []
        etime = []
        for elem in intervals:
            stime.append(elem[0])
            etime.append(elem[1])
        stime.sort()
        etime.sort()
        
        rooms = 0
        sptr,eptr = 0,0
        
        while sptr < len(stime):
            if stime[sptr] >= etime[eptr]:
                rooms-=1
                eptr+=1
            
            rooms+=1
            sptr+=1
                
        return rooms
