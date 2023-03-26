class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         # 1. 얘는 시간은 O(n)이긴 하고 대신 공간을 O(n) 만큼 먹음.
#         steps = k % len(nums)
        
#         tmp = []
#         for i in range(len(nums)-steps):
#             tmp.append(nums[i])
        
#         for i in range(steps):
#             j = len(nums) - steps + i
#             nums[i] = nums[j]
        
#         for i in range(steps, len(nums)):
#             j = i - steps
#             nums[i] = tmp[j]
        # 2. reverse 이용. 왼쪽 오른쪽 각각 뒤집고 또 전체를 뒤집으면 됨
        def reverse(left, right):
            _left, _right = left, right
            while _left < _right:
                nums[_left], nums[_right] = nums[_right], nums[_left]
                _left += 1
                _right -= 1
        
        steps = k % len(nums)
        # 각각 reverse
        reverse(0, len(nums)-steps-1)
        reverse(len(nums)-steps, len(nums)-1)
        # 전체 reverse
        reverse(0, len(nums)-1)
        