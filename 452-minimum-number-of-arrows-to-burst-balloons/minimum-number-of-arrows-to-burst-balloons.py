class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = 1
        points.sort(key=lambda x: x[1])
        arrow_pos = points[0][1]
        for start, end in points:
            if start > arrow_pos:
                res += 1
                arrow_pos = end
        return res