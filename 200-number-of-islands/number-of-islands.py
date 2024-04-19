class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or grid[r][c] != "1":
                return
            visited.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    count += 1
        return count