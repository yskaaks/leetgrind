class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        fresh_oranges = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh_oranges += 1
        time = 0
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while q and fresh_oranges > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    fresh_oranges -= 1
                    q.append((row, col))
            time += 1
        return time if fresh_oranges == 0 else -1














        # q = collections.deque()

        # fresh_oranges = 0
        # rows, cols = len(grid), len(grid[0])
        # for row in range(rows):
        #     for col in range(cols):
        #         if grid[row][col] == 2:
        #             q.append((row, col))
        #         elif grid[row][col] == 1:
        #             fresh_oranges += 1
        # time = 0
        # directions = [[0,1], [0, -1], [1,0], [-1, 0]]

        # while q and fresh_oranges > 0:
        #     for i in range(len(q)):
        #         r, c = q.popleft()

        #         for dr, dc in directions:
        #             row, col = dr + r, dc + c
        #             if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] != 1:
        #                 continue
        #             grid[row][col] = 2
        #             q.append((row, col))
        #             fresh_oranges -= 1
        #     time += 1
        # if fresh_oranges == 0:
        #     return time
        # return -1