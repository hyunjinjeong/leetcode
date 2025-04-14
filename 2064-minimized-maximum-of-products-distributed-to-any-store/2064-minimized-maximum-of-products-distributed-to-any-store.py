class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # quantity마다 나누기를 해야 하는데.. 어떻게 하면 최적의 나눗셈을 찾을 수 있을까?
        # 아 binary search임

        def can_distribute(amt):
            stores = 0
            for quantity in quantities:
                stores += math.ceil(quantity / amt)
                if stores > n:
                    return False
            return True
        
        lo, hi = 1, max(quantities)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if can_distribute(mid): # 즉 amt가 충분히 크단 얘기
                hi = mid
            else:
                lo = mid + 1
        
        return lo