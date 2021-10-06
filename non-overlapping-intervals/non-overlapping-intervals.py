class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        
        intervals.sort()
        new_interval = [intervals[0]]
        
        for i in range(1, len(intervals)) :
            if new_interval[-1][1] > intervals[i][0] :
                if new_interval[-1][1] >= intervals[i][1] :
                    new_interval[-1] = intervals[i]
            else :
                new_interval.append(intervals[i])
                
        return len(intervals) - len(new_interval)
                    