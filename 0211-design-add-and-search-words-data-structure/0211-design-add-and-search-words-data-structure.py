class WordDictionary:

    def __init__(self):
        self.root = Node(None)

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node(c)
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        # .이면 하나 건너뛰고 children 모두 돌면 되려나?
        # 결국 dfs 였다 ㄷㄷ
        def dfs(node, i):
            if i == len(word):
                return node.is_word
            
            if word[i] == '.':
                for c in node.children:
                    if dfs(node.children[c], i+1):
                        return True
                return False
            else:
                if word[i] not in node.children:
                    return False
                return dfs(node.children[word[i]], i+1)
        
        return dfs(self.root, 0)


class Node:
    
    def __init__(self, key):
        self.key = key
        self.children = {}
        self.is_word = False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)