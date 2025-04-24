class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # # num의 최대 길이가 9고 각 digit은 한 번만 써야 함
        # # 그냥 backtracking으로 풀면 될 것 같은데? 최대 경우의 수는 9!
        # length = len(pattern) + 1
        
        # def backtrack(curr, used_digits):
        #     i = len(curr)
        #     if i == length:
        #         self.res = min(self.res, "".join(curr))
        #         return
            
        #     prev_pattern, prev_num = pattern[i - 1], curr[i - 1]
        #     for digit in range(1, 10):
        #         num = str(digit)
        #         if num in used_digits:
        #             continue

        #         if prev_pattern == "I" and num <= prev_num:
        #             continue
        #         if prev_pattern == "D" and num >= prev_num:
        #             continue
                
        #         curr.append(num)
        #         used_digits.add(num)
        #         backtrack(curr, used_digits)
        #         curr.pop()
        #         used_digits.remove(num)
        
        # self.res = "9" * length
        # for digit in range(1, 10):
        #     backtrack([str(digit)], set(str(digit)))
        # return self.res

        # 오.. stack도 됨
        res = []
        stack = []
        for i in range(len(pattern) + 1):
            stack.append(str(i + 1))
            while stack and (i == len(pattern) or pattern[i] == "I"):
                res.append(stack.pop())
        return "".join(res)
