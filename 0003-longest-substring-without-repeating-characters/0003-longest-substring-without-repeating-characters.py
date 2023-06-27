class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # counter 정의해서... sliding window?
        pos = {}
        ans = 0

        left = 0
        for right, c in enumerate(s):
            if c not in pos:
                ans = max(right - left + 1, ans)
            else:
                if pos[c] < left:
                    ans = max(right - left + 1, ans)
                else:
                    left = pos[c] + 1
            
            pos[c] = right

        return ans