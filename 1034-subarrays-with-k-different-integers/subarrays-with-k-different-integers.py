class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMostKDistinct(nums, k) - self.atMostKDistinct(nums, k-1)
    

    def atMostKDistinct(self, nums, k):
        count, left = 0, 0
        freq_table = collections.defaultdict(int)

        for right in range(len(nums)):
            
            freq_table[nums[right]] += 1

            while len(freq_table) > k:
                freq_table[nums[left]] -= 1
                if freq_table[nums[left]] == 0:
                    del freq_table[nums[left]]
                left += 1
            count += right - left + 1
        return count
