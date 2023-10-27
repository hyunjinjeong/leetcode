class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def to_int(c):
            return ord(c) - ord("0")
        
        if num1 == "0" or num2 == "0":
            return "0"
        
        N, M = len(num1), len(num2)
        
        ans = [0] * (N + M - 1)
        for i, n1 in enumerate(num1):
            for j, n2 in enumerate(num2):
                ans[i + j] += to_int(n1) * to_int(n2)
        
        for i in range(len(ans) - 1, 0, -1):
            ans[i - 1] += ans[i] // 10
            ans[i] %= 10

        return "".join([str(n) for n in ans])
        