class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        last_mink = last_max_k = last_invalid = -1
        count = 0

        for i, num in enumerate(nums):
            if num == minK:
                last_mink = i
            if num == maxK:
                last_max_k = i
            
            if num < minK or num > maxK:
                last_invalid = i
            count += max(0, min(last_max_k, last_mink) - last_invalid)
        return count