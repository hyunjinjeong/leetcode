class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        n0, n1, n2 = 0, 1, 1
        for _ in range(n - 3):
            n0, n1, n2 = n1, n2, n0 + n1 + n2
        
        return n0 + n1 + n2