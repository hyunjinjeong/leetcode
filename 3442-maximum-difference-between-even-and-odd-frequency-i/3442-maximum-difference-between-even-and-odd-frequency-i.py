class Solution:
    def maxDifference(self, s: str) -> int:
        freq = [0] * 26
        
        for c in s:
            freq[ord(c) - ord("a")] += 1
        
        max_odd, min_even = 0, float("inf")
        for i in range(26):
            if freq[i] == 0:
                continue

            if freq[i] % 2 == 1:
                max_odd = max(max_odd, freq[i])
            else:
                min_even = min(min_even, freq[i])
        
        return max_odd - min_even
