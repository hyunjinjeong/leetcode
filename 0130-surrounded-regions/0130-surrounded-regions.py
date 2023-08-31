class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 이것도 문제를 거꾸로 생각해보면 O인 edge에서부터 도달할 수 있는 것들을 거르면 됨.
        M, N = len(board), len(board[0])
        
        for row in range(M):
            self.dfs(row, 0, board)
            self.dfs(row, N - 1, board)
        
        for col in range(N):
            self.dfs(0, col, board)
            self.dfs(M - 1, col, board)
        
        for r in range(M):
            for c in range(N):
                if board[r][c] == "#":
                    board[r][c] = "O"
                elif board[r][c] == "O": # O로 남아있는 것들은 surrounded
                    board[r][c] = "X"
    
    def dfs(self, x, y, board):
        if board[x][y] != "O":
            return

        board[x][y] = "#" # visited 역할도 하고...
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < len(board) and 0 <= next_y < len(board[0]):
                self.dfs(next_x, next_y, board)