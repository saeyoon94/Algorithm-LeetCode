class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals :
            return [newInterval]
        
        index = bisect.bisect_right(intervals, newInterval)
    
        def merge(interval1, interval2) :
            if interval1[1] >= interval2[0] :
                return [min(interval1[0],interval2[0]), max(interval1[1],interval2[1])]
            return False
        
        unchecked = True
        
        if index == len(intervals) :
            merged = merge(intervals[-1], newInterval)
            unchecked = False
            if merged :
                intervals[-1] = merged
            else :
                intervals.append(newInterval)
                
        if index == 0 and unchecked :
            merged = merge(newInterval, intervals[0])
            if merged :
                intervals[index] = merged
                unchecked = False
                while True :
                    if index < len(intervals) - 1 :
                        merged_next = merge(intervals[index], intervals[index+1])
                        if merged_next :
                            intervals = [merged_next] + intervals[index+2:]
                        else :
                            break
                    else :
                        break
            
        
        if index-1 >= 0 and unchecked :
            merged = merge(intervals[index-1], newInterval)
            if merged :
                intervals[index-1] = merged
                unchecked = False
                while True :
                    if index < len(intervals) :
                        merged_next = merge(intervals[index-1], intervals[index])
                        if merged_next :
                            intervals = intervals[:index-1] + [merged_next] + intervals[index+1:]
                        else :
                            break
                    else :
                        break
        
        if unchecked :
            merged = merge(newInterval, intervals[index])
            if merged :
                intervals[index] = merged
                unchecked = False
                while True :
                    if index+1 < len(intervals) :
                        merged_next = merge(intervals[index], intervals[index+1])
                        if merged_next :
                            intervals = intervals[:index] + [merged_next] + intervals[index+2:]
                        else :
                            break
                    else :
                        break
                
        if unchecked :
            intervals = intervals[:index] + [newInterval] + intervals[index:]
        
        return intervals
        