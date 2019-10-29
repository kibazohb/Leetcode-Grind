class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals = sorted(intervals, key = lambda x: x[0])
        out = []
        out.append(intervals[0])
        
        idx = 0
        for ptr in range (1,len(intervals)):
            last = out[-1]
            if intervals[ptr][0] <= last[1]:
                last[1] = max(intervals[ptr][1], last[1])
            else:
                out.append(intervals[ptr])

        return out    
