class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # silding window... 마지막으로 c가 사용된 위치 저장하면 된당
        last_used = {}
        max_length, start = 0, 0
        
        for i, c in enumerate(s):
            if c in last_used and start <= last_used[c]:
                start = last_used[c] + 1
            else:
                max_length = max(max_length, i-start+1)
            
            last_used[c] = i
        
        return max_length