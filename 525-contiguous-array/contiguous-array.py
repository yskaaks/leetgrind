class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0:-1}
        res = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1

            if count in d:
                res = max(res, i-d[count])
            else:
                d[count] = i
        return res