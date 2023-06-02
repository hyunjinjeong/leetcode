class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        
        ans = 0
        stack.append(-1)
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    ans = max(ans, i - stack[-1])
                else:
                    stack.append(i)
        
        return ans