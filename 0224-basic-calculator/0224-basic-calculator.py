class Solution:
    def calculate(self, s: str) -> int:
        res = 0

        num, sign, stack = 0, 1, []
        for c in s:
            if c.isdigit():
                num = num * 10 + (ord(c) - ord("0"))
            elif c in "+-":
                res += sign * num
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(res)
                stack.append(sign) # 이게 핵심.. 괄호 표현식 전체의 부호를 stack에 넣어둬서 활용
                res, sign = 0, 1
            elif c == ")":
                res += sign * num
                res *= stack.pop() # sign
                res += stack.pop()
                num = 0
        
        return res + sign * num
