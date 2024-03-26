class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        smallest_positive = 1

        for num in nums:
            if num == smallest_positive:
                smallest_positive += 1
        return smallest_positive