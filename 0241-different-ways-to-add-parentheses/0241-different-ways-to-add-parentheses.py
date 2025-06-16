class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # operator 마다 좌우로 나눠서 모든 경우의 수를 계산하면.. 될 것 같은데

        def dfs(start, end):
            if start == end:
                return [ops[start]]

            curr = []
            for i in range(start, end + 1):
                if not (ops[i] == "+" or ops[i] == "-" or ops[i] == "*"):
                    continue
                
                left = dfs(start, i - 1)
                right = dfs(i + 1, end)
                
                for left_operand in left:
                    for right_operand in right:
                        if ops[i] == "+":
                            curr.append(left_operand + right_operand)
                        elif ops[i] == "-":
                            curr.append(left_operand - right_operand)
                        else:
                            curr.append(left_operand * right_operand)

            return curr

        ops = []
        curr_num = 0
        for c in expression:
            if c in "+-*":
                ops.append(curr_num)
                ops.append(c)
                curr_num = 0
            else:
                curr_num = curr_num * 10 + int(c)
        ops.append(curr_num)

        return dfs(0, len(ops) - 1)
