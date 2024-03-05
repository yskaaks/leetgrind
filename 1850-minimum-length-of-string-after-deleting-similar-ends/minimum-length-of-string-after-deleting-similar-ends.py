class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            curr_char = s[left]
            
            while left <= right and curr_char == s[left]:
                left += 1
            while left <= right and curr_char == s[right]:
                right -= 1
        return right - left + 1 