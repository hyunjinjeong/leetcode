class Solution:
    def calculate(self, s: str) -> int:
        # infix -> postfix 아이디어인데.. in place로도 가능함.
        precendence = {"+": 1, "-": 1, "*": 2, "/": 2}
        
        operators = []
        nums = []
        i = 0
        while i < len(s):
            if "0" <= s[i] <= "9":
                curr_num = 0
                while i < len(s) and "0" <= s[i] <= "9":
                    curr_num = curr_num * 10 + ord(s[i]) - ord("0")
                    i += 1
                nums.append(curr_num)
            elif s[i] in "+-*/":
                while operators and precendence[operators[-1]] >= precendence[s[i]]:
                    print(nums, operators)
                    self.cal(nums, operators)
                    print(nums, operators)
                operators.append(s[i])
                i += 1
            else:
                i += 1
                continue
        
        # 마지막 계산이 남아 있음.
        while operators:
            self.cal(nums, operators)
        
        return nums.pop()
    
    def cal(self, nums, operators):
        op = operators.pop()
        right = nums.pop()
        left = nums.pop()
        if op == "+":
            tmp = left + right
        elif op == "-":
            tmp = left - right
        elif op == "*":
            tmp = left * right
        else:
            tmp = left // right
        nums.append(tmp)