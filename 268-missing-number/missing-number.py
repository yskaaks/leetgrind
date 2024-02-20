class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)
        
        for num in s:
            if (num-1) >= 0 and  (num-1) not in s:
                return num - 1
        return max(s) + 1