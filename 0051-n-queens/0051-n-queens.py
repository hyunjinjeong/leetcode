class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 대표적인 backtracking 문제..
        # 퀸은 대각선 포함 모든 방향으로 이동할 수 있음.
        # valid면 놓고 아니면 빼고...
        # row 단위로 이동하기.
        
        def is_valid(row, col):
            # upper column
            for r in range(row):
                if board[r][col] == "Q":
                    return False
            # upper left diagonal
            for i in range(n):
                if row - i >= 0 and col - i >= 0:
                    if board[row-i][col-i] == "Q":
                        return False
            # upper right diagonal
            for i in range(n):
                if row - i >= 0 and col + i < n:
                    if board[row-i][col+i] == "Q":
                        return False
            return True
        
        def dfs(row):
            if row == n:
                ans.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if is_valid(row, col):
                    board[row][col] = "Q"
                    dfs(row + 1)
                    board[row][col] = "."
        
        ans = []
        board = [["."] * n for _ in range(n)]
        dfs(0)
        
        return ans