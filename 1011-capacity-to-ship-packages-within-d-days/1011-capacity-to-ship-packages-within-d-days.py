class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # binary search로 안 되려나?
        def is_satisfied(target_weight):
            curr_weight, curr_day = 0, 1
            for weight in weights:
                if weight > target_weight:
                    return False
                
                if curr_weight + weight > target_weight:
                    curr_day += 1
                    curr_weight = weight
                else:
                    curr_weight += weight
                
                if curr_day > days:
                    return False
            
            return True

        total_weights = sum(weights)
        
        lo, hi = 0, total_weights
        while lo < hi:
            mid = (lo + hi) // 2

            if is_satisfied(mid):
                hi = mid
            else:
                lo = mid + 1
        
        return lo
                    