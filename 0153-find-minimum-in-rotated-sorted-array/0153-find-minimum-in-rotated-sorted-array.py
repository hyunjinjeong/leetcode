class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search를 응용하면 될 것 같은데
        # rotate 된 부분을 기준으로
        # left도 정렬, right도 정렬
        # mid가 right보다 크면 오른쪽, 아니면 왼쪽으로 가면 됨.
        # 1 2 3 4 5
        # 5 1 2 3 4
        # 4 5 1 2 3
        # 3 4 5 1 2
        # 2 3 4 5 1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]