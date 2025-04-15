class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # brute force는 O(NMK)인가? 근데 어떻게 최적화하징
        # word1을 words2 전체와 비교하지 않고 한번에 할 방법이 있을까...
        # count의 max를 다 저장해두는건 어떨까? 될 것 같은데
        words2_max_counter = collections.defaultdict(int)
        for word2 in words2:
            word2_counter = collections.defaultdict(int)
            for c in word2:
                word2_counter[c] += 1
            
            for c in word2_counter:
                words2_max_counter[c] = max(words2_max_counter[c], word2_counter[c])
        
        res = []
        for word1 in words1:
            word1_counter = collections.defaultdict(int)
            for c in word1:
                word1_counter[c] += 1
            
            is_universal = True
            for c in words2_max_counter:
                if word1_counter[c] < words2_max_counter[c]:
                    is_universal = False
                    break
            
            if is_universal:
                res.append(word1)
        
        return res
