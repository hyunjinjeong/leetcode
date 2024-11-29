class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # 원래 문제랑 별 차이 없을거 같은데
        # 아 안되는 경우가 있네
        # 그러면..
        # pivot을 먼저 찾고.
        # pivot의 left, right에 대해서 binary search를 수행하면 될 듯
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2

            if nums[mid] >= nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        
        pivot = lo
        print("pivot", pivot)

        
        def bisect(lo, hi):
            l, r = lo, hi
            while l < r:
                mid = (l + r) // 2

                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            
            print("left", l)
            return nums[l] == target
        
        left = bisect(0, pivot - 1)
        right = bisect(pivot, len(nums) - 1)

        return left or right