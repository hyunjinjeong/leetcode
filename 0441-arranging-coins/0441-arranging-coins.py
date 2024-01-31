class Solution:
    def arrangeCoins(self, n: int) -> int:
        # binary search를 사용할 수 있다
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            curr_sum = mid * (mid + 1) // 2

            if curr_sum == n:
                return mid

            if curr_sum > n:
                r = mid - 1
            else:
                l = mid + 1
        
        return r