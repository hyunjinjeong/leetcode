class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            # ans += n & 1
            # n >>= 1
            # n & n - 1을 하는 방법도 있음. 그러면 가장 오른쪽의 1이 사라짐.
            # e.g. 1100 & 1011 == 1000
            n = n & n - 1
            ans += 1
        return ans