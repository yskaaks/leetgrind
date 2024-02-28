class Solution:
    def largestPalindromic(self, num: str) -> str:
        counts = [0] * 10
        for digit in num:
            counts[int(digit)] += 1
        
        first_half = []
        for digit in range(9, -1,-1):
            if digit == 0 and not first_half:
                # avoiding leading zeros
                break
            count = counts[digit] // 2
            first_half.extend([str(digit)] * count)
            counts[digit] -= count * 2
        
        # find the middle digit, which is the largest possible unused digit
        mid_digit = ''
        for digit in range(9, -1,-1):
            if counts[digit] > 0:
                mid_digit = str(digit)
                break
        second_half = first_half[::-1] # mirroring the first first_half
        palindrome = ''.join(first_half) + mid_digit + ''.join(second_half)

        if not palindrome or palindrome == '0' * len(palindrome):
            return '0'
        return palindrome