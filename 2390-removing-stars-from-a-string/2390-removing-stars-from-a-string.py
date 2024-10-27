class Solution:
    def removeStars(self, s: str) -> str:
        # stack을 쓰면 되려나?
        stack = []

        for c in s:
            if c == "*":
                stack.pop()
            else:
                stack.append(c)
        
        return "".join(stack)