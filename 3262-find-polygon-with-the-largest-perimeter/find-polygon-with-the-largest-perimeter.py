class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        res = -1
        for i in nums:
            if i < total:
                res = total + i 
            total += i
        return res