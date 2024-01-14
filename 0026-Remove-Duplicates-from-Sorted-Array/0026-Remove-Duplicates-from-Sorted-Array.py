class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        nxt = 1
        while i < len(nums):

            if nums[nxt-1] != nums[i]:
                nums[nxt] = nums[i]
                nxt += 1
            i += 1
        return nxt
