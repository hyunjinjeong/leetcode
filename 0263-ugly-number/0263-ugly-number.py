class Solution:
    def isUgly(self, n: int) -> bool:
        # 어떤 숫자가 2, 3, 5로만 나눠지면 ugly
        # 7부터.. sqrt(n)까지 소수를 모두 구해서 n이 나눠지는지 확인하면 됨 => TLE
        # 2, 3, 5로 계속 나눠서 1이 되는지 확인하면 된댜.
        if n <= 0:
            return False
        
        def divide(target):
            num = n
            while num % target == 0:
                num //= target
            return num
        
        n = divide(2)
        n = divide(3)
        n = divide(5)
        
        return n == 1