class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        depth = 0
        for c in s:
            if c == "(":
                depth += 1
                res = max(res, depth)
            elif c == ")":
                depth -= 1
        
        return res