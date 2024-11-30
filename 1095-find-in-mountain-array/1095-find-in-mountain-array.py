# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # so I need to somehow use the characteristic of mountainArr.
        # the total calls should be less than 100. And the length <= 10**4 so O(logn) algorithm is needed.
        # 1. Find the peak element, let's call the index of the peak element P
        # 2. Run bisect on both sides, [0, P-1] and [P+1, N-1]
        # 3. Return min()        
        def find_peak_index():
            left, right = 1, mountainArr.length() - 2
            while left <= right:
                mid = left + (right - left) // 2
                
                mid_num = mountainArr.get(mid)
                left_num = mountainArr.get(mid - 1)
                right_num = mountainArr.get(mid + 1)

                if left_num < mid_num and mid_num > right_num:
                    return mid

                if left_num > mid_num: # peak is on the left side
                    right = mid - 1
                else:
                    left = mid + 1

        def bisect(start, end, reverse=False):
            left, right = start, end
            while left <= right:
                mid = left + (right - left) // 2
            
                mid_num = mountainArr.get(mid)
                if mid_num == target:
                    return mid

                if reverse:
                    if mid_num > target: # target is on the right side
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if mid_num > target: # target is on the left side
                        right = mid - 1
                    else:
                        left = mid + 1
            
            return -1
        
        peak = find_peak_index()
        
        left_side = bisect(0, peak)
        if left_side >= 0:
            return left_side

        right_side = bisect(peak + 1, mountainArr.length() - 1, reverse=True)
        if right_side >= 0:
            return right_side

        return -1