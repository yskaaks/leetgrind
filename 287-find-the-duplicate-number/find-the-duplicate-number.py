class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # using set but not constant space
        # duplicates = set()
        # for i in nums:
        #     if i in duplicates:
        #         return i
        #     duplicates.add(i)

        # nlogn complexity need to optimize
        nums.sort()
        for i in range(len(nums) + 1):
            if nums[i] == nums[i+1]:
                return nums[i]
        return 0










