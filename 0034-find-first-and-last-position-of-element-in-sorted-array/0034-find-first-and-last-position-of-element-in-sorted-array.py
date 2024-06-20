class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 누가 봐도 binary search 문제임
        def bisect_left():
            index = -1
            lo, hi = 0, len(nums) - 1
            
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    index = mid
                    hi = mid - 1
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            
            return index
        
        def bisect_right():
            index = -1
            lo, hi = 0, len(nums) - 1
            
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    index = mid
                    lo = mid + 1
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            
            return index
        
        return [bisect_left(), bisect_right()]