class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0] * n for _ in range(n)]
        for j in range(n):
            dp[0][j] = grid[0][j]
        
        for i in range(1, n):
            for j in range(n):
                min_prev = float("inf")
                for k in range(n):
                    if k != j:
                        min_prev = min(min_prev, dp[i-1][k])
                dp[i][j] = grid[i][j] + min_prev
        return min(dp[-1])

        # if len(grid) == 1:
        #     return min(grid[0])
        # memo = {}
        # def dfs(i, prev_col):
        #     if i == len(grid) - 1:
        #         return grid[i][prev_col]
        #     if (i, prev_col) in memo:
        #         return memo[(i, prev_col)]
        #     min_path_sum = float("inf")
        #     for col in range(len(grid)):
        #         if col != prev_col:
        #             curr_path_sum = grid[i][col] + 1 + dfs(i+1, col)
        #             min_path_sum = min(min_path_sum, curr_path_sum)
        #     memo[(i, prev_col)] = min_path_sum
        #     return min_path_sum
        # return min(dfs(0, col) for col in range(len(grid)))
