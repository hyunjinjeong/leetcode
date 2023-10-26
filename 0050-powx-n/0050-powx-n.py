class Solution:
    def myPow(self, x: float, n: int) -> float:
        # TLE가 뜨는걸로 봐선... 최적화가 필요함
        # x^(2y) = x^y * x^y 요걸 활용해보자. 홀수면 x^(2y+1) = x^y * x^y * x 요런 식으로.
        if n < 0:
            x = 1 / x
            n = -n
        
        cache = {}
        def calc(num, e):
            if e == 0:
                return 1
            if e == 1:
                return num
            if (num, e) in cache:
                return cache[(num, e)]

            if e % 2 == 0:
                ans = calc(num, e // 2) * calc(num, e // 2)
            else:
                ans = calc(num, e // 2) * calc(num, e // 2) * calc(num, 1)
            
            cache[(num, e)] = ans
            return ans
        
        return calc(x, n)