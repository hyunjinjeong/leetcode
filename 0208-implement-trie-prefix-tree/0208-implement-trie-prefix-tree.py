class Trie:

    def __init__(self):
        self.root = Node(None)

    def insert(self, word: str) -> None:
        node = self.root
        
        for c in word:
            if c not in node.children:
                child = Node(c)
                node.children[c] = child
            node = node.children[c]

        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        
        return node.is_word
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        
        return True
        

class Node:
    def __init__(self, c):
        self.c = c
        self.is_word = False
        self.children = {}

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)