class Solution:
    def calculate(self, s: str) -> int:
        # infix -> postfix로 바꿔서 계산하면 될 듯?
        postfix = []
        operators = []
        
        # infix -> postfix로 바꾸기
        precendence = {"+": 1, "-": 1, "*": 2, "/": 2}
        i = 0
        while i < len(s):
            if "0" <= s[i] <= "9":
                curr_num = 0
                while i < len(s) and "0" <= s[i] <= "9":
                    curr_num = curr_num * 10 + ord(s[i]) - ord("0")
                    i += 1
                postfix.append(curr_num)
            elif s[i] in ("+", "-", "*", "/"):
                while operators and precendence[operators[-1]] >= precendence[s[i]]:
                    postfix.append(operators.pop())
                operators.append(s[i])
                i += 1
            else:
                i += 1
                continue
        
        while operators:
            postfix.append(operators.pop())
        
        # postfix 계산
        stack = []
        for item in postfix:
            if item not in ("+", "-", "*", "/"):
                stack.append(item)
            else:
                right = stack.pop()
                left = stack.pop()
                if item == "+":
                    tmp = left + right
                elif item == "-":
                    tmp = left - right
                elif item == "*":
                    tmp = left * right
                else:
                    tmp = left // right
                stack.append(tmp)

        return stack.pop()