class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return 1
            if (r,c) in visited:
                return 0
            visited.add((r,c))
            perimeter = 0
            perimeter += dfs(r+1, c)
            perimeter += dfs(r-1, c)
            perimeter += dfs(r, c+1)
            perimeter += dfs(r, c-1)

            return perimeter
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    return dfs(row, col)
        return 0
    
