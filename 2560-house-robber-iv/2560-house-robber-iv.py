class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # max의 min을 찾는건 보통 binary search임. but how?
        # 그냥 돌면 되나..
        def is_possible(limit):
            i = 0
            count = 0
            while i < len(nums):
                if nums[i] <= limit:
                    count += 1
                    i += 2
                else:
                    i += 1
                
                if count >= k:
                    return True
            return False
        
        lo, hi = min(nums), max(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            if is_possible(mid):
                hi = mid
            else:
                lo = mid + 1
        
        return lo
