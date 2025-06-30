class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # 대놓고 trie를 쓰는 문제 같은데
        # path를 지나갈 때마다 count를 1씩 증가시키면 되나?
        # abc -> a에 1, b에 1, c에 1
        # ab -> a에 2, b에 2
        # bc -> b에 1, c에 1
        # b -> b에 2
        # 최종적으로 (a, 2) -> (b, 2) -> (c, 1)이랑 (b, 2) -> (c, 1)
        # 그러고 쭉 돌면서 세면 될 듯?
        # abc -> 2 2 1 = 5
        # ab -> 2 2 = 4
        # bc -> 2 1 = 3
        # b -> 2 = 2
        trie = Trie()
        for word in words:
            trie.add(word)
        
        return [trie.count(word) for word in words]

class Trie:
    def __init__(self):
        self.root = TrieNode(None)
    
    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]
            node.count += 1
    
    def count(self, word):
        total = 0
        node = self.root
        for c in word:
            node = node.children[c]
            total += node.count
        return total

class TrieNode:
    def __init__(self, char):
        self.children = {}
        self.char = char
        self.count = 0
