class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1
        maxx = 0
        for freq in d.values():
            maxx = max(freq, maxx)
        
        freq_of_max_freq = 0
        for freq in d.values():
            if freq == maxx:
                freq_of_max_freq += 1
        
        return freq_of_max_freq * maxx