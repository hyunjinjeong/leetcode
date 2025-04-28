class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ")":
                reversed_substring = []
                while stack and stack[-1] != "(":
                    reversed_substring.append(stack.pop())
                stack.pop() # "("
                stack.extend(reversed_substring)
            else:
                stack.append(c)

        return "".join(stack)
