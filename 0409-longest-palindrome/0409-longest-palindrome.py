class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = collections.defaultdict(int)
        for c in s:
            counter[c] += 1
        
        res = 0
        has_odd = False
        for count in counter.values():
            if count % 2 == 0:
                res += count
            else:
                res += count - 1
                has_odd = True
        
        return res + 1 if has_odd else res