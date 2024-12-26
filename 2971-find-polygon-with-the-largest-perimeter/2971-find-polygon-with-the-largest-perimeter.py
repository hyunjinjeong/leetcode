class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # 정렬하고 prefix sum..?
        # prefix_sum[i - 1]이 num보다 큰지를 보면 됨
        # 이 때 값은 prefix_sum[i - 1] + num == prefix_sum[i]
        nums.sort()
        
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        res = -1
        for i in range(2, len(nums)):
            if prefix_sum[i] > nums[i]:
                res = prefix_sum[i + 1]

        return res