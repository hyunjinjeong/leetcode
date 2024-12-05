class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        # def find_leftmost_eligible_index(prefix):
        #     l, r = 0, len(products) - 1
        #     while l < r:
        #         mid = l + (r - l) // 2
                
        #         if products[mid] >= prefix:
        #             r = mid
        #         else:
        #             l = mid + 1
            
        #     return l
        
        # products.sort()
        
        # res = []
        # prefix = ""
        # for c in searchWord:
        #     prefix += c
        #     i = find_leftmost_eligible_index(prefix)
        #     res.append([word for word in products[i:i + 3] if word.startswith(prefix)])

        # return res

        # Trie 버전...
        class TrieNode:
            def __init__(self):
                self.children = collections.defaultdict(TrieNode)
                self.suggestions = []
            
            def add_suggestion(self, product):
                if len(self.suggestions) < 3:
                    self.suggestions.append(product)
        
        products.sort()

        root = TrieNode()
        for product in products:
            node = root
            for char in product:
                node = node.children[char]
                node.add_suggestion(product)
        
        res, node = [], root
        for char in searchWord:
            node = node.children[char]
            res.append(node.suggestions)
        
        return res
