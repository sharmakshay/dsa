from collections import defaultdict


class Solution:

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row_seen = defaultdict(set)
        col_seen = defaultdict(set)
        sq_seen = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == ".":
                    continue

                if val in row_seen[i] or val in col_seen[j] or val in sq_seen[(
                        i // 3, j // 3)]:
                    return False

                row_seen[i].add(val)
                col_seen[j].add(val)
                sq_seen[(i // 3, j // 3)].add(val)

        return True
