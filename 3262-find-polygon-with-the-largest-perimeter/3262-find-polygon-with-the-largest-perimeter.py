class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # 정렬하고 prefix sum..?
        # prefix_sum[i - 1]이 num보다 큰지를 보면 됨
        # 이 때 값은 prefix_sum[i - 1] + num == prefix_sum[i]
        # 근데 prefix sum도 필요가 없구나
        nums.sort()
        
        prefix_sum = 0
        res = -1
        for num in nums:
            if prefix_sum > num:
                res = prefix_sum + num
            prefix_sum += num

        return res