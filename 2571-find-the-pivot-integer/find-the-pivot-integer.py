class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = sum(range(1, n + 1))


        prefix = 0
        for i in range(1, n + 1):
            total_sum -= i
            if total_sum == prefix:
                return i
            prefix +=i
        return -1
