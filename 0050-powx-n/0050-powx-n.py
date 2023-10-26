class Solution:
    def myPow(self, x: float, n: int) -> float:
        # TLE가 뜨는걸로 봐선... 최적화가 필요함
        # x^(2y) = (x^2)^y 요걸 활용해보자. 홀수면 x^(2y+1) = x^2y * x 요런 식으로.
        # def calc(num, e):
        #     if e < 0:
        #         return 1 / calc(num, -e)
        #     if e == 0:
        #         return 1
        #     if e == 1:
        #         return num

        #     if e % 2 == 0:
        #         return calc(num * num, e // 2)
        #     else:
        #         return num * calc(num, e - 1)
        
        # return calc(x, n)

        # iterative 버전
        if n < 0:
            x = 1 / x
            n = -n
        
        ans = 1
        while n:
            if n % 2 == 1:
                ans *= x
            
            x *= x
            n = n // 2
        
        return ans