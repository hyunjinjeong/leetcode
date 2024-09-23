class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        def dfs(num):
            if num <= 26:
                return chr(ord("A") + num - 1)
            
            quotient, remainder = num // 26, num % 26
            if remainder == 0:
                return dfs(quotient - 1) + dfs(26)
            else:
                return dfs(quotient) + dfs(remainder)

        return dfs(columnNumber)