class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        length = float("inf")
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                length = min(right - left + 1, length)
                current_sum -= nums[left]
                left += 1
        if length == float("inf"):
            return 0
        else:
            return length
