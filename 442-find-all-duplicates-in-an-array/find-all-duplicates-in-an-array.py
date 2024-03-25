class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        res = []
        for key, value in d.items():
            if value == 2:
                res.append(key)
        return res