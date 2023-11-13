class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # 규칙을 찾아야 하는데
        # 일단 자릿수를 먼저 봐야겠지? 자릿수가 적을수록 낮은 숫자고
        # 그다음에는 큰 자릿수부터 작은 숫자가 최소.
        # ..? 주제가 greedy네
        stack = []
        attempts = 0

        for n in num:
            while stack and stack[-1] > n and attempts < k:
                stack.pop()
                attempts += 1
            stack.append(n)
        
        while attempts < k:
            stack.pop()
            attempts += 1

        return "".join(stack).lstrip("0") or "0"
