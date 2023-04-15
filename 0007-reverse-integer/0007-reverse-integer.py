class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        
        # 음수 처리
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
        
        while x:
            ans = ans * 10 + x % 10
            x //= 10
            
        ans *= sign
        return ans if -2**31 <= ans <= 2**31 - 1 else 0