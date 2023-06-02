class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        
        ans = 0
        # stack에는 현재 index에서 valid한 마지막 위치가 들어감.
        stack.append(-1) 
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack: # stack이 남아 있으면 valid란 소리..
                    ans = max(ans, i - stack[-1])
                else: # 이제 invalid. 그러면 새 index를 push
                    stack.append(i)
        
        return ans