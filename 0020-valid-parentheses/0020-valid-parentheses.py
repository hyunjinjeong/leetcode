class Solution:
    def isValid(self, s: str) -> bool:
        # 단순하게 스택 이용해서 구현
        open_parens = []
        pairs = { "}": "{", "]": "[", ")": "(" }
        
        for c in s:
            if c == "(" or c == "[" or c == "{":
                open_parens.append(c)
            else:
                if not open_parens or pairs[c] != open_parens[-1]:
                    return False
                open_parens.pop()
                
        return not open_parens
        