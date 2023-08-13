class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Trie?
        # words를 Trie 형태로 저장한 다음에
        # board는 DFS 돌리면 될 듯?
        # 접근은 맞는데 쌩 Trie는 TLE가 뜬다. 여러 최적화 써서 시간을 줄여야 함.
        ...
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        self.ans = []
        for x in range(len(board)):
            for y in range(len(board[0])):
                c = board[x][y]
                self.dfs(board, trie.root.children.get(c), x, y, c)
        
        return self.ans
        
    def dfs(self, board, node, x, y, curr):
        if not node:
            return

        if node.is_word:
            self.ans.append(curr)
            node.is_word = False # 중복 방지.
        
        c = board[x][y]
        board[x][y] = "-" # visited
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < len(board) and 0 <= next_y < len(board[0]):
                next_c = board[next_x][next_y]
                self.dfs(board, node.children.get(next_c), next_x, next_y, curr + next_c)
        board[x][y] = c


class Trie:
    def __init__(self):
        self.root = TrieNode(None)
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]
        node.is_word = True


class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_word = False
