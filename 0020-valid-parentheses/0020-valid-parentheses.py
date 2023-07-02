class Solution:
    def isValid(self, s: str) -> bool:
        # 단순하게 스택 이용해서 구현
        stack = []
        pairs = { "}": "{", "]": "[", ")": "(" }
        
        for c in s:
            if c in ("(", "[", "{"):
                stack.append(c)
            else:
                if not stack or pairs[c] != stack[-1]:
                    return False
                stack.pop()
                
        return not stack
        