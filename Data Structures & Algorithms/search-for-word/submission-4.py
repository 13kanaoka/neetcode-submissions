class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(row, col, i, visit):
            if i >= len(word):
                return True
            if (row < 0 or col < 0 or row >= ROWS or col >= COLS or
                (row, col) in visit or board[row][col] != word[i]):
                return False

            visit.add((row, col))
            res = (dfs(row - 1, col, i + 1, visit) or
                    dfs(row + 1, col, i + 1, visit) or
                    dfs(row, col - 1, i + 1, visit) or
                    dfs(row, col + 1, i + 1, visit))
            visit.remove((row, col))
            return res

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0, set()):
                    return True
        return False