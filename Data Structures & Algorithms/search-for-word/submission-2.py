class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def backtrack(row, col, i):
            if i == len(word):
                return True
            if (row < 0 or col < 0 or row >= ROWS or col >= COLS or
                (row, col) in path) or word[i] != board[row][col]:
                return False

            path.add((row, col))
            res = (backtrack(row + 1, col, i + 1) or
                    backtrack(row - 1, col, i + 1) or
                    backtrack(row, col + 1, i + 1) or
                    backtrack(row, col - 1, i + 1))
            path.remove((row, col))
            return res


        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]:
                    if backtrack(row, col, 0):
                        return True

        return False