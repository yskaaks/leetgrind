class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and (row,col) not in visited:
                    if self.dfs(board, row, col, visited, word, 0):
                        return True
        return False

    def dfs(self, board, row, col, visited, word, i):
        if len(word) == i:
            return True
        if (row, col) in visited or row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or word[i] != board[row][col]:
            return False
        visited.add((row,col))

        found = self.dfs(board, row+1, col, visited, word, i+1) or self.dfs(board, row-1, col, visited, word, i+1) or self.dfs(board, row, col+1, visited, word, i+1) or self.dfs(board, row, col-1, visited, word, i+1)
        visited.remove((row,col))
        return found


















    #     rows, cols = len(board), len(board[0])

    #     visited = set()
    #     for row in range(rows):
    #         for col in range(cols):
    #             if word[0] == board[row][col] and (row, col) not in visited:
    #                 if self.dfs(board, row, col, visited, word, 0):
    #                     return True
    #     return False
    
    # def dfs(self, board, row, col, visited, word, i):
    #     if i == len(word):
    #         return True
    #     if row < 0 or col < 0 or row == len(board) or col == len(board[0]) or (row, col) in visited or word[i] != board[row][col]:
    #         return False
    #     visited.add((row, col))

    #     found = self.dfs(board, row+1, col, visited, word, i+1) or self.dfs(board, row-1, col, visited, word, i+1) or self.dfs(board, row, col+1, visited, word, i+1) or self.dfs(board, row, col-1, visited, word, i+1)
    #     visited.remove((row,col))
    #     return found
