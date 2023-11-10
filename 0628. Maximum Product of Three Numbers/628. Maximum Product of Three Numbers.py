class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        tmp1 = sorted(nums, reverse=True)
        prod1 = 1
        for i in tmp1[:3]:
            prod1 *= i
        tmp2 = sorted(nums)
        prod2 = 1
        for i in tmp2[:2]:
            prod2 *= i
        prod2 *= tmp1[0]
        return max(prod1, prod2)
