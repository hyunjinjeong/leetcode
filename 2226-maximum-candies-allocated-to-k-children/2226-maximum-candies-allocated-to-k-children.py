class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # 흠 [4, 7, 5], k=4 같은 경우엔 4가 아니라 3이구나
        # 캔디 갯수 C에 대해, candies[i] // C의 값만큼 n명에게 C개를 나눠줄 수 있게 됨
        # 아 그르면 C의 최댓값을 찾는 문제겠네... binary search다

        def can_allocate(c):
            if not c:
                return True

            allocated = 0
            for candy in candies:
                allocated += candy // c
                if allocated >= k:
                    return True

            return False
        
        # if len(candies) == 1:
        #     return candies[0] // k
        
        lo, hi = 0, max(candies)
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2

            if can_allocate(mid):
                lo = mid
            else:
                hi = mid - 1
        
        return lo
