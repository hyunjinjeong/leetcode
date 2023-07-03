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
                # truncate toward zero.
                # Python에선 -1 // 2 == -1 이 되기 때문에...
                return int(left / right) 

        # 간단하게 stack 쓰면 되지 않나?
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