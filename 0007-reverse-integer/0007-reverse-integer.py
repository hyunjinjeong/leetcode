class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        
        is_negative = False
        if x < 0:
            is_negative = True
            x = -x
        
        while x:
            remainder = x % 10
            ans = ans * 10 + remainder
            x //= 10
            
        ans = -ans if is_negative else ans
        return ans if -2**31 <= ans <= 2**31 - 1 else 0