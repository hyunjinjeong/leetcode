class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            r, c = rMove + dr, cMove + dc
            size = 2
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == "." or board[r][c] == color and size < 3:
                    break
                if board[r][c] == color:
                    return True
                r += dr
                c += dc
                size += 1

        return False