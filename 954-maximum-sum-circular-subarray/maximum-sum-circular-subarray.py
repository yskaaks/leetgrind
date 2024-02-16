class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max = 0
        cur_min = 0
        max_sum = nums[0]
        min_sum = nums[0]
        total = 0

        for num in nums:
            cur_max = max(0, cur_max) + num
            cur_min = min(0, cur_min) + num

            max_sum = max(max_sum, cur_max)
            min_sum = min(min_sum, cur_min)

            total += num
        if max_sum < 0:
            return max_sum
        return max(max_sum, total - min_sum)