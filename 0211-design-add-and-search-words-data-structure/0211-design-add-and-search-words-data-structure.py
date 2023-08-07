class WordDictionary:

    def __init__(self):
        self.root = TrieNode(None)

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        return self.dfs(word, 0, self.root)
    
    # . 일때는 하나 건너뛰고 grand children을 모두 보면 됨
    def dfs(self, word, index, node):
        if index == len(word):
            return node.is_word
        
        c = word[index]
        if c == ".":
            for key in node.children:
                if self.dfs(word, index + 1, node.children[key]):
                    return True
            return False
        else:
            if c not in node.children:
                return False
            return self.dfs(word, index + 1, node.children[c])

class TrieNode:
    def __init__(self, val):
        self.val = val
        self.is_word = False
        self.children = {}

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)