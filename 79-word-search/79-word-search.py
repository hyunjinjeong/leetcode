class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 딱 봐도 backtracking 쓰는 문제 같긴 한데...
        # 방향은 맞았는데 다른 데서 시간을 많이 쓴 듯? moves for문 없애고 set 안 쓰고 하니까 됨.
        # 근데 제대로 코드 짜도 자꾸 TLE 뜸;
        self.board = board
        self.word = word
        self.found = False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.found:
                    return True
                self.dfs(r, c, 0)
        
        return self.found
    
    def dfs(self, r, c, index):
        if self.found:
            return
        
        if index == len(self.word):
            self.found = True
            return

        if r < 0 or c < 0 or r >= len(self.board) or c >= len(self.board[0]):
            return
        if self.board[r][c] != self.word[index]:
            return

        char = self.board[r][c]
        self.board[r][c] = "-" # visited
        self.dfs(r+1, c, index+1)
        self.dfs(r-1, c, index+1)
        self.dfs(r, c+1, index+1)
        self.dfs(r, c-1, index+1)
        self.board[r][c] = char