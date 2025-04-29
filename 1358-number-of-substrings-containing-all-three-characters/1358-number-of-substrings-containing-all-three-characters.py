class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # sliding window 인데
        # 한번 abc를 가지면 오른쪽 구간은 전부 해당됨. 길이만큼 더하면 될 듯.
        res = 0
        
        counts = {"a": 0, "b": 0, "c": 0}
        left = 0
        for right in range(len(s)):
            counts[s[right]] += 1
            while all(counts[c] > 0 for c in counts):
                res += len(s) - right
                counts[s[left]] -= 1
                left += 1

        return res
