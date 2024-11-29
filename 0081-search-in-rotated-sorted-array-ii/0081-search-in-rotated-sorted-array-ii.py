class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # # 원래 문제랑 별 차이 없을거 같은데
        # # 아 안되는 경우가 있네
        # # 그러면..
        # # pivot을 먼저 찾고.
        # # pivot의 left, right에 대해서 binary search를 수행하면 될 듯
        # # pivot을 binary search로 못 찾겠네... 그러면 이건 loop로 돌자

        # pivot = 0
        # for i in range(1, len(nums)):
        #     if nums[i] < nums[i - 1]:
        #         pivot = i
        #         break
        
        # def bisect(lo, hi):
        #     l, r = lo, hi
        #     while l < r:
        #         mid = (l + r) // 2

        #         if nums[mid] >= target:
        #             r = mid
        #         else:
        #             l = mid + 1

        #     return nums[l] == target
        
        # left = bisect(0, pivot - 1)
        # right = bisect(pivot, len(nums) - 1)

        # return left or right

        # binary search를 쓸 수는 있구나
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return True

            if nums[lo] < nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            elif nums[lo] > nums[mid]:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid
            else:
                lo += 1
        
        return nums[lo] == target