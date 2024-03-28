class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq_table = collections.defaultdict(int)
        max_len = float("-inf")
        left = 0
        for right in range(len(nums)):
            freq_table[nums[right]] += 1

            while freq_table[nums[right]] > k:

                freq_table[nums[left]] -= 1
                if freq_table[nums[left]] == 0:
                    del freq_table[nums[left]]
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len