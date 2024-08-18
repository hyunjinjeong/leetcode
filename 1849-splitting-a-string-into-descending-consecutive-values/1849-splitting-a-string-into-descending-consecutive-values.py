class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(start, prev):
            if start == len(s):
                return True
            
            for i in range(start, len(s)):
                curr = int(s[start:i + 1])
                if prev - curr == 1 and dfs(i + 1, curr):
                    return True
            
            return False
        
        for i in range(len(s) - 1):
            val = int(s[:i + 1])
            if dfs(i + 1, val):
                return True
        
        return False