class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # 이건 걍 two pointer 쓰면 될 듯?
        res, curr = 0, 0

        left = 0
        for right in range(len(s)):
            if s[right] in "aeiou":
                curr += 1
            
            if right - left + 1 > k:
                if s[left] in "aeiou":
                    curr -= 1
                left += 1
            
            res = max(res, curr)
        
        return res
        