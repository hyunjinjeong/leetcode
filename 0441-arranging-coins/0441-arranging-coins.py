class Solution:
    def arrangeCoins(self, n: int) -> int:
        # 1 -> 2 -> 3 -> 4 -> 5 -> ... 이런 식으로 늘어나니까
        # n에서 빼면서 계산하면 될 듯

        i = 1
        while i <= n:
            n -= i
            i += 1

        return i - 1