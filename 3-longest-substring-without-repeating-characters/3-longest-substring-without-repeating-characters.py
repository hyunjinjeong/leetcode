class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        
        answer = 0
        left, i = 0, 0
        
        # 일단 naive하게..
        # 중복이 있을 때마다 left를 한칸씩 뒤로 가면 되지 않을까.
        while left < len(s) and i < len(s):
            c = s[i]            
            if c in chars:
                answer = max(answer, i-left)
                
                chars.clear()
                left += 1
                i = left
            else:
                answer = max(answer, i-left+1)
                chars.add(c)
                i += 1
            
        return answer