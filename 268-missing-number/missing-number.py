class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        
        for num in counter:
            # if (num + 1) not in counter:
            #     return num + 1
            if (num-1) >= 0 and  (num-1) not in counter:
                return num - 1
        return max(counter) + 1