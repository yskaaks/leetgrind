class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        count_max_element = 0
        left = 0
        count = 0
        freq_table = collections.defaultdict(int)

        for right in range(len(nums)):
            if nums[right] == max_element:
                count_max_element += 1
            while count_max_element == k:
                if nums[left] == max_element:
                    count_max_element -= 1
                left += 1
            count += left
        return count