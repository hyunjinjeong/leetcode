class Solution:
    def reverseBits(self, n: int) -> int:
        # 아.. 길이가 32인 binary string 인거에 주목!
        result = 0
        for i in range(32):
            result = (result << 1) + (n & 1)
            n = n >> 1
        return result