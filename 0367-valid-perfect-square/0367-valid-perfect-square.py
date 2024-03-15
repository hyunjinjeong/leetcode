class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        lo, hi = 1, num
        while lo < hi:
            mid = (lo + hi) // 2

            if mid * mid == num:
                return True
            
            if mid * mid > num:
                hi = mid
            else:
                lo = mid + 1
            
        return False