class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # sliding window 인데
        # 한번 abc를 가지면 오른쪽 구간은 전부 해당됨. 길이만큼 더하면 될 듯.
        total = 0
        freq = [0, 0, 0]
        
        left = 0
        for right in range(len(s)):
            freq[ord(s[right]) - ord("a")] += 1
            while all(value > 0 for value in freq):
                total += len(s) - right
                freq[ord(s[left]) - ord("a")] -= 1
                left += 1

        return total
