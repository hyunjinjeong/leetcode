class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        # (rMove, cMove) 값을 color로 바꿨을 때
        # (rMove, cMove)가 good line의 endpoint여야 legal임
        # good line은 길이 3 이상으로, 양 끝 cell의 색이 같고, 나머지 cell들의 색은 반대로 같아야 함
        # 그럼 상하좌우 그리고 대각선 상하좌우... 8방향으로 해당 조건을 만족하는지 보면 되려나?
        def check(r, c, dr, dc, length):
            if r >= 8 or r < 0 or c >= 8 or c < 0:
                return False

            res = True
            if board[r][c] == ".":
                res = False
            elif board[r][c] == color:
                res = length >= 2
            else:
                res = check(r + dr, c + dc, dr, dc, length + 1)
            return res

        res = (check(rMove, cMove + 1, 0, 1, 1)
            or check(rMove, cMove - 1, 0, -1, 1)
            or check(rMove + 1, cMove, 1, 0, 1)
            or check(rMove - 1, cMove, -1, 0, 1)
            or check(rMove + 1, cMove + 1, 1, 1, 1)
            or check(rMove + 1, cMove - 1, 1, -1, 1)
            or check(rMove - 1, cMove + 1, -1, 1, 1)
            or check(rMove - 1, cMove - 1, -1, -1, 1))

        return res