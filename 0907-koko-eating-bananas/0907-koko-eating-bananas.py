class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search...

        def can_eat_all(k):
            hours = 0
            for pile in piles:
                if k >= pile:
                    hours += 1
                else:
                    hours += math.ceil(pile / k)
            return hours <= h
        
        ans = float("inf")
        left, right = 1, max(piles) + 1
        while left < right:
            mid = (left + right) // 2
            if can_eat_all(mid):
                ans = min(mid, ans)
                right = mid
            else:
                left = mid + 1

        return ans