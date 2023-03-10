class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
#         # 딱 봐도 backtracking 쓰는 문제 같긴 한데...
#         # 코드 맞게 짜도 자꾸 TLE 떴다가 안 떴다가 함
#         def dfs(r, c, length):
#             if length == len(word):
#                 return True
            
#             if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
#                 return False
#             if board[r][c] == "":
#                 return False
#             if board[r][c] != word[length]:
#                 return False
            
#             char = board[r][c]
#             board[r][c] = "" # visited
#             result = dfs(r+1, c, length+1) or dfs(r-1, c, length+1) or dfs(r, c+1, length+1) or dfs(r, c-1, length+1)
#             board[r][c] = char
            
#             return result

#         for r in range(len(board)):
#             for c in range(len(board[0])):
#                 if dfs(r, c, 0):
#                     return True
        
#         return False
        # 아래는 follow up인 pruning 활용. pruning은 그냥 엣지 케이스들 대비해서 미리 체크하는 정도.
        def dfs(r, c, length):
            if length == len(word):
                return True
            
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False
            if board[r][c] == "":
                return False
            if board[r][c] != word[length]:
                return False
            
            char = board[r][c]
            board[r][c] = "" # visited
            result = dfs(r+1, c, length+1) or dfs(r-1, c, length+1) or dfs(r, c+1, length+1) or dfs(r, c-1, length+1)
            board[r][c] = char
            
            return result
        
        # Pruning/Edge case #1 - Check if a word length is longer than the matrix itself
        if len(word) > len(board) * len(board[0]):
            return False;
        
        # Pruning/Edge case #2 - Check if all needed characters for the word are on the board
        charFreq = {};
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] not in charFreq:
                    charFreq[board[r][c]] = 0
                charFreq[board[r][c]] += 1
        
        for char in word:
            if char not in charFreq:
                return False;
            charFreq[char] -= 1
            
            if charFreq[char] == 0:
                del charFreq[char]
        
        # Pruning 다 통과하면 이제 메인 알고리즘으로..
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True