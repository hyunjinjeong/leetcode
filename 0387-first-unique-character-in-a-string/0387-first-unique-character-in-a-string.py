class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = collections.Counter(s)
        
        for i, c in enumerate(s):
            if freq[c] == 1:
                return i
        
        return -1