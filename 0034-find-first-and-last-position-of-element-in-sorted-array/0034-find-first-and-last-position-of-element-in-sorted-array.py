class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 누가 봐도 binary search 문제임
        def bisect_left(t):
            lo, hi = 0, len(nums)
            
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < t:
                    lo = mid + 1
                else:
                    hi = mid
            
            return lo
        
        ans = [-1, -1]
        
        ans[0] = bisect_left(target)
        ans[1] = bisect_left(target + 1) - 1
        
        if ans[0] <= ans[1]:
            return ans
        
        return [-1, -1]