class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        empty = [["."] * n for _ in range(n)]
        return self.backtrack(0, empty, n, [])
    
    # row 단위로...
    # 왼쪽 대각선 위, 오른쪽 대각선 위, 위로 있는지 세 가지 경우 확인 필요.
    def backtrack(self, row, curr, n, ans):
        if row == n:
            ans.append(["".join(s) for s in curr])
            return ans
        
        for col in range(n):
            if self.can_place_queen(row, col, curr):
                curr[row][col] = "Q"
                self.backtrack(row + 1, curr, n, ans)
                curr[row][col] = "."
        
        return ans
    
    def can_place_queen(self, row, col, curr):
        return self.check_upper(row, col, curr) and self.check_left_diagonal(row, col, curr) and self.check_right_diagonal(row, col, curr)
    
    def check_upper(self, row, col, curr):
        r = row - 1
        while r >= 0:
            if curr[r][col] == "Q":
                return False
            r -= 1
        return True
    
    def check_left_diagonal(self, row, col, curr):
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if curr[r][c] == "Q":
                return False
            r -= 1
            c -= 1
        return True
    
    def check_right_diagonal(self, row, col, curr):
        r, c = row - 1, col + 1
        while r >= 0 and c < len(curr):
            if curr[r][c] == "Q":
                return False
            r -= 1
            c += 1
        return True