class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def reverse(start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        reverse(0, len(s) - 1)
        start = 0
        for right in range(len(s)):
            if s[right] == " ":
                reverse(start, right - 1)
                start = right + 1
        reverse(start, len(s) - 1) # reverse last word
