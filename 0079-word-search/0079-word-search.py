class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtrack(i, j, 0, board, word):
                    return True
        
        return False
    
    def backtrack(self, x, y, index, board, word):
        if board[x][y] != word[index]:
            return False
        
        if index == len(word) - 1:
            return True
    
        val = board[x][y]
        board[x][y] = '-'

        result = False
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < len(board) and 0 <= next_y < len(board[0]):
                result = self.backtrack(next_x, next_y, index + 1, board, word) or result
        
        board[x][y] = val
        return result