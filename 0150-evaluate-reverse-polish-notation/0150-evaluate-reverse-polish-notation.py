class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def eval(operator, left, right):
            if operator == "+":
                return left + right
            if operator == "-":
                return left - right
            if operator == "*":
                return left * right
            if operator == "/":
                return int(left / right)

        # stack 쓰면 되지 않나?
        stack = []
        for token in tokens:
            if token in "+-*/":
                right = stack.pop()
                left = stack.pop()
                
                result = eval(token, left, right)
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack.pop()