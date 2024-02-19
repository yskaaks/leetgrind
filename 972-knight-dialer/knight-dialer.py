class Solution:
    def knightDialer(self, n: int) -> int:
        moves = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4],
        }
        memo = {}

        def helper(start_digit, length):
            if length == 1:
                return 1
            if (start_digit, length) in memo:
                return memo[(start_digit, length)]
            total = 0
            for next_digit in moves[start_digit]:
                total += helper(next_digit, length - 1)
            memo[(start_digit, length)] = total % (10**9 + 7)
            return memo[(start_digit, length)]
        return sum(helper(digit, n) for digit in range(10)) % (10**9 + 7)
