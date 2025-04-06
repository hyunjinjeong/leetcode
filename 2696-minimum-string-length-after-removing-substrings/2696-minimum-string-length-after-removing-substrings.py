class Solution:
    def minLength(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        for i in range(len(s)):
            sub = s[i:i+2]
            if sub in ("AB", "CD"):
                return self.minLength(s[:i] + s[i+2:])
        
        return len(s)