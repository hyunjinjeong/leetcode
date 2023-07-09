class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search...
        # find minimum in rotated 와 비슷하다.
        # nums[mid] > nums[right]면 현재 rotated된 상태인 건데...  그럼 두 경우 각각 생각해보자.
        # target을 찾기 위해서 left, right 어디를 줄여야 하는지 찾아야 함.
        # 1. nums[mid] > nums[right]인 경우
        # target < nums[mid]면? target > nums[right]면 right를 줄이고, 아니면 left를 줄이고
        # target > nums[mid]면? 이 경우는 무조건 left를 올려야 할 것 같은데
        # 2. nums[mid] < nums[right]인 경우
        # target < nums[mid]면? right를 줄이고..
        # target > nums[mid]면? 여기도 마찬가지로 target > nums[right]면 right를 줄이고, 아니면 left를 줄이면 되지 않을까.
        # [4 5 6 0 1 2 7]
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > nums[hi]:
                if target < nums[mid]:
                    if target > nums[hi]:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                else:
                    lo = mid + 1
            else:
                if target > nums[mid]:
                    if target > nums[hi]:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                else:
                    hi = mid - 1
        
        return -1