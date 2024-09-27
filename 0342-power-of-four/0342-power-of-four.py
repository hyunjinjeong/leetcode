class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # loop, recursion 없이는 bit 연산인거 같은데
        # 1 / 100 / 10000 / 1000000 이런 식으로 감.
        # 그러면 일단 n - 1 이랑 and를 해서 0이 되어야 함. 그러면 2의 제곱이 되고
        # 여기서 4의 제곱은 2진수로 나타냈을 때 길이가 홀수면 됨
        if n == 0:
            return False
        return n & (n - 1) == 0 and len(bin(n)) % 2 == 1