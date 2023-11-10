class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_max, cur_min = 1, 1

        for i in nums:
             
            tmp = cur_max * i
            cur_max = max(i, tmp, cur_min * i)
            cur_min = min(i, tmp, cur_min * i)

            res = max(cur_max, res)
        return res
