class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 아.. 그냥 x**n을 계산하면 곱하기를 n번 해야 하니까 횟수를 줄이는게 포인트.
        # 예를 들어 5**10 = 5**5 * 5**5. O(logn)이 됨.
        
        # edge cases
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        # 홀수인 경우.
        if n % 2 == 1:
            return x * self.myPow(x, n-1)
        
        return self.myPow(x*x, n//2)