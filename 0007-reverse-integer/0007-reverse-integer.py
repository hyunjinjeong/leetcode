class Solution:
    def reverse(self, x: int) -> int:
#         ans = 0
        
#         # 음수 처리
#         if x < 0:
#             sign = -1
#             x = -x
#         else:
#             sign = 1
        
#         while x:
#             ans = ans * 10 + x % 10
#             x //= 10
            
#         ans *= sign
#         return ans if -2**31 <= ans <= 2**31 - 1 else 0
    
        # 위 코드는 좋지만 64비트 자료형을 사용하기 때문에...
        ans = 0
        
        # 음수 처리
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
        
        MAX_INT, MIN_INT = 2**31-1, -2**31
        while x:
            # MAX_INT: 2147483647 이니까.
            if sign == 1 and (ans > MAX_INT // 10 or ans == MAX_INT // 10 and x % 10 > 7):
                return 0
            # MIN_INT: -2147483648. 양수로 만들어줬기 때문에 해당 부분 고려
            # Python에서 음수 나누기는 이런식으로..
            if sign == -1 and (-ans < math.ceil(MIN_INT / 10) or -ans == math.ceil(MIN_INT / 10) and -(x % 10) < -8):
                return 0
            
            ans = ans * 10 + x % 10
            x //= 10
        
        return ans * sign