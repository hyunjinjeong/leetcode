class Solution:
    def findMin(self, nums: List[int]) -> int:
        # sorted array면 binary search...
        # rotated면 pivot 기준으로 왼쪽도 단조 증가, 오른쪽도 단조 증가한다.
        # nums[left] > nums[right]면 중간 어딘가에 pivot이 있다는 의미
        # 반대로 nums[left] < nums[right]면 그 구간은 sorted된 상태인 건데...
        # 그러면 min을 찾는 방법은 또 뭘까
        # mid를 고려해보자
        # nums[mid] > nums[right]면 최솟값이 오른쪽 구간에 있는 건가?
        # 이 조건으로만 봐도 되는 건가?
        
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2

            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid

        return nums[lo]