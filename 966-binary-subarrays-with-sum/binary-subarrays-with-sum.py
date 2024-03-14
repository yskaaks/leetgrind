class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        d = {0:1}
        prefix_sum = 0

        for num in nums:
            prefix_sum += num

            if prefix_sum - goal in d:
                res += d[prefix_sum-goal]
            
            if prefix_sum in d:
                d[prefix_sum] += 1
            else:
                d[prefix_sum] = 1
        return res