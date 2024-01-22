class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])

        q = collections.deque()
        visited = set()

        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == 0:
                    q.append([row,col])
                    visited.add((row,col))
        

        while q:
            r, c = q.popleft()
            # up
            if r > 0 and rooms[r-1][c] == 2147483647:
                rooms[r-1][c] = rooms[r][c] + 1
                q.append([r-1, c])
            if r < rows - 1 and rooms[r+1][c] == 2147483647:
                rooms[r+1][c] = rooms[r][c] + 1
                q.append([r+1, c])
            if c > 0 and rooms[r][c-1] == 2147483647:
                rooms[r][c-1] = rooms[r][c] + 1
                q.append([r, c-1])
            if c < cols - 1 and rooms[r][c+1] == 2147483647:
                rooms[r][c+1] = rooms[r][c] + 1
                q.append([r, c+1])
            