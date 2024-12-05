class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # 3 product names after each character.
        # common prefix with searchWord. more than three -> three lexicographically minimums.
        # Trie..? 가 직관적으로 떠오르긴 하는데
        # 근데 생각해보니 Trie는 중간 단계에서 어떻게 리턴을 해주지
        # 각 단계마다 모든 단어를 저장해두기..?
        # 일단 sort를 한번 해두고 처리하면 될 듯

        # a ab b bc bcd bcde 이러면
        # prefix가 bc면... 

        products.sort()

        def find_leftmost_eligible_index(prefix):
            # 일단 binary search 써보자
            l, r = 0, len(products) - 1
            while l < r:
                mid = l + (r - l) // 2
                
                if products[mid] >= prefix:
                    r = mid
                else:
                    l = mid + 1
            
            return l
        
        
        res = []

        prefix = ""
        for c in searchWord:
            prefix += c
            i = find_leftmost_eligible_index(prefix)
            curr = []
            while len(curr) < 3 and i < len(products) and products[i].startswith(prefix):
                curr.append(products[i])
                i += 1
            res.append(curr)

        return res

        # trie = {}
        # for product in products:
        #     build_trie(product)
        
        # def build_trie(s):
        #     curr = trie
        #     for c in s:
        #         if c in curr:
        #             curr[c] = ...
        #         else:
        #             curr[c] = [] # 데이터 하나에는 s를 넣고, 하나는 다시 타고 들어가고.. 그런 식으로 해야 하는데