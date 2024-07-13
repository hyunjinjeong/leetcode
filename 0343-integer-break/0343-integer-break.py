class Solution:
    def integerBreak(self, n: int) -> int:
        # 이게 dp가 성립하나?
        # 2는 1*1 = 1이고
        # 3은 2*1 = 2
        # 4는 2*2 = 4
        # 5는 2*3 = 6
        # 6은 3*3 = 9
        # 7은 3*2*2 = 12
        # 8은 3*3*2 = 18
        # 9는 3*3*3 = 27
        # 10은 3*3*4 = 36
        # 11은 3*3*3*2 = 54
        # 규칙성이 안보이는데...
        # 최대한 3을 많이 넣고 남은건 2로 채우면 되는 느낌이기도 하고?
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        ans = 1
        while n:
            if n - 3 >= 2:
                ans *= 3
                n -= 3
            else:
                ans *= 2
                n -= 2

        return ans 