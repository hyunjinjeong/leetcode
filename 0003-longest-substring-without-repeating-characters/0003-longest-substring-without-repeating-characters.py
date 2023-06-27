class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # counter 정의해서... sliding window?
        last_pos = {}
        ans = 0

        left = 0
        for right, c in enumerate(s):
            if c not in last_pos:
                ans = max(right - left + 1, ans)
            else:
                if last_pos[c] < left:
                    ans = max(right - left + 1, ans)
                else:
                    left = last_pos[c] + 1
            
            last_pos[c] = right

        return ans