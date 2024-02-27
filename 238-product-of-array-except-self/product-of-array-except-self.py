class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # fill the left array
        for i in range(1, n):
            res[i] = nums[i-1] * res[i-1]
        right = 1
        for i in range(n-1, -1,-1):
            res[i] *= right
            right *= nums[i]
        return res