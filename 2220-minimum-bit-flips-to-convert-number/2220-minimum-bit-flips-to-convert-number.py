class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = 0

        # 1010
        # 0111
        # 1101

        xor = start ^ goal
        while xor:
            res += 1
            xor &= xor - 1

        return res