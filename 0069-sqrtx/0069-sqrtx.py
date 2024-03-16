class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        lo, hi = 0, x
        while lo < hi:
            mid = (lo + hi) // 2

            if mid * mid > x:
                hi = mid
            else:
                lo = mid + 1
        
        return lo - 1