class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0 for _ in range(n)] for _ in range(m)]

        
        for i in range(n):
            dp[0][i] = 1
        for j in range(m):
            dp[j][0] = 1
        

        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


        # prev_row = [0] * n

        # for row in range(m - 1, -1, -1):
        #     cur_row = [0] * n
        #     cur_row[n - 1] = 1
        #     for col in range(n - 2, -1, -1):
        #         cur_row[col] = prev_row[col] + cur_row[col + 1]
        #     prev_row = cur_row
        # return prev_row[0]





        # def dfs(r, c, row, col):
        #     if r == row or c == col:
        #         return 0
        #     if r == row - 1 or c == col - 1:
        #         return 1
        #     return dfs(r + 1, c, row, col) + dfs(r, c+1, row, col)
        # return dfs(0,0,m,n)
         