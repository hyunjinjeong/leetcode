class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 딱 봐도 backtracking 쓰는 문제 같긴 한데...
        # 아래처럼 하면 TLE가 뜬다.
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(r, c, length):
            if length == len(word):
                return True
            
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False
            if board[r][c] is True:
                return False
            if board[r][c] != word[length]:
                return False
            
            char = board[r][c]
            board[r][c] = True # visited
            result = dfs(r+1, c, length+1) or dfs(r-1, c, length+1) or dfs(r, c+1, length+1) or dfs(r, c-1, length+1)
            board[r][c] = char
            
            return result

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        
        return False