class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search... O(NlogM) 이겠다.
        def eating_time(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours
        
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if eating_time(mid) > h:
                left = mid + 1
            else:
                right = mid
        return left