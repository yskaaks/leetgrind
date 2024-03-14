class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        return self.helper(nums, goal) - self.helper(nums, goal-1)
    
    def helper(self, nums, goal):
        if goal < 0:
            return 0
        left = 0
        ssum = 0
        res = 0
        for right in range(len(nums)):
            ssum += nums[right]
            while ssum > goal:
                ssum -= nums[left]
                left += 1
            res += right - left + 1
        return res
        # res = 0
        # d = {0:1}
        # prefix_sum = 0

        # for num in nums:
        #     prefix_sum += num

        #     if prefix_sum - goal in d:
        #         res += d[prefix_sum-goal]
            
        #     if prefix_sum in d:
        #         d[prefix_sum] += 1
        #     else:
        #         d[prefix_sum] = 1
        # return res