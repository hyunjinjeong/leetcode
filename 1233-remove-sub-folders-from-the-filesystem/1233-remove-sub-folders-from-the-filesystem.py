class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # trie 만들기?
        trie = Trie()
        for path in folder:
            trie.insert(path)

        return [path for path in folder if trie.is_root(path)]


class Node:
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.is_path = False


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, path):
        node = self.root
        for name in path.split("/"):
            if name == "":
                continue
            if name not in node.children:
                node.children[name] = Node(name)
            node = node.children[name]
        node.is_path = True

    def is_root(self, path):
        node = self.root
        folders = path.split("/")
        for i, name in enumerate(folders):
            if name == "" or i == len(folders) - 1:
                continue
            node = node.children[name]
            if node.is_path:
                return False
        return True
