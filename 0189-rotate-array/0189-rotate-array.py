class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k를 생각해보면
        # k % len(nums) 경우만 고려하면 되지 않을까? 
        # 즉 len(nums)가 7이면
        # 0, 7
        # 1, 8 ... 뭐 이런 식으로
        
        steps = k % len(nums)
        
        tmp = []
        for i in range(len(nums)-steps):
            tmp.append(nums[i])
        
        for i in range(steps):
            j = len(nums) - steps + i
            nums[i] = nums[j]
        
        for i in range(steps, len(nums)):
            j = i - steps
            nums[i] = tmp[j]