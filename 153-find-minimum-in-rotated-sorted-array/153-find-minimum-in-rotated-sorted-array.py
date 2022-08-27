class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 이거 binary search 쓰면 되지 않으려나?
        # 더 작은 쪽으로 계속 좁혀가다 보면 최솟값이 나오지 않을지..
        
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]