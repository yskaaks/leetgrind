class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # O(nlogn) time, O(1) space
        nums.sort()
        res = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                res.append(nums[i])
        
        return res



        # O(N) time and space
        # d = {}
        # for num in nums:
        #     if num in d:
        #         d[num] += 1
        #     else:
        #         d[num] = 1
        # res = []
        # for key, value in d.items():
        #     if value == 2:
        #         res.append(key)
        # return res