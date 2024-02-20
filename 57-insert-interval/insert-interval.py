class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        start, end = 0, 1
        i = 0
        # before the merge 
        while i < len(intervals) and intervals[i][end] < newInterval[start]:
            res.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i][start] <= newInterval[end]:
            newInterval[start] = min(newInterval[start], intervals[i][start])
            newInterval[end] = max(newInterval[end], intervals[i][end])
            i += 1
        res.append(newInterval)
        # rest of the list
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        return res