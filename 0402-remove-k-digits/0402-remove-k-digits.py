class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # 규칙을 찾아야 하는데
        # 일단 자릿수를 먼저 봐야겠지? 자릿수가 적을수록 낮은 숫자고
        # 그다음에는 큰 자릿수부터 작은 숫자가 최소.
        # ..? 주제가 greedy네
        stack = []
        attempts = 0

        for n in num:
            # monotonic increasing stack 이용
            while stack and stack[-1] > n and attempts < k:
                stack.pop()
                attempts += 1
            stack.append(n)
        
        # 12345... 같은 경우 k가 안 줄어듦. 그러면 마지막부터 빼주면 됨.
        while attempts < k:
            stack.pop()
            attempts += 1

        return "".join(stack).lstrip("0") or "0"
