class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # O(logn)은 binary search 밖에 안 떠오르는데
        # 적어도 하나의 peak가 있다고 치면
        # peak의 특징은.. 왼쪽이 자기보다 작고 오른쪽도 자기보다 작은거
        # 그러면 리턴하면 되고
        # 왼쪽이 자기보다 크다? 그러면 왼쪽으로 가면 됨
        # 반대면 오른쪽으로 가면 되려나?

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            
            left_num = nums[mid - 1] if mid > 0 else float("-inf")
            right_num = nums[mid + 1] if mid < len(nums) - 1 else float("-inf")
            
            if nums[mid] < left_num:
                right = mid - 1
            elif nums[mid] < right_num:
                left = mid + 1
            else:
                return mid
            
            