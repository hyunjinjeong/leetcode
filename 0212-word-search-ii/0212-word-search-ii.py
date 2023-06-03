class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # trie?
        # words를 trie로 만들어서 저장한 다음에
        # board에서 board[x][y]가 trie root인 경우에만 dfs 돌림
        # 쌩 trie는 TLE 떠서.. 최적화 필요함.
        
        # 단순하게 dict로 trie 구현
        trie = {}
        for word in words:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['#'] = True # is_word
        
        self.ans = []
        for x in range(len(board)):
            for y in range(len(board[0])):
                c = board[x][y]
                self.dfs(board, trie.get(c), c, x, y)
        return self.ans
    
    def dfs(self, board, node, path, x, y):
        if not node:
            return
        
        if '#' in node: # is_word
            self.ans.append(path)
            del node['#'] # 중복 방지
        
        tmp = board[x][y]
        board[x][y] = "#" # visited
        
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < len(board) and 0 <= next_y < len(board[0]) and board[next_x][next_y] != "#":
                c = board[next_x][next_y]
                self.dfs(board, node.get(c), path + c, next_x, next_y)
                
        board[x][y] = tmp