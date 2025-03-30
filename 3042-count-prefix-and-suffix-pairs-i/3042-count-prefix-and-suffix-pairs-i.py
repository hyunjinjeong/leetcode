class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        def is_prefix(w1, w2):
            if len(w1) > len(w2):
                return False

            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    return False
            return True
        
        def is_suffix(w1, w2):
            if len(w1) > len(w2):
                return False
            
            i, j = len(w1) - 1, len(w2) - 1
            while i:
                if w1[i] != w2[j]:
                    return False
                i -= 1
                j -= 1
            return True
        
        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if is_prefix(words[i], words[j]) and is_suffix(words[i], words[j]):
                    res += 1
        return res