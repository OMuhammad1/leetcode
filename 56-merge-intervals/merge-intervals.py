class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = [] 
        intervals.sort()

        for interval in intervals:
            if not merged:
                merged.append(interval)
            if merged[-1][1] >= interval[0]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)
            
        return merged
        