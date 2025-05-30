class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # i번째 인덱스를 기준으로 왼쪽의 합이 오른쪽의 합보다 커야 된다는 뜻이네. i는 왼쪽에 속하고
        # 걍 prefix sum 문제네
        left_prefix_sum, right_prefix_sum = 0, sum(nums)

        res = 0
        for i in range(len(nums) - 1):
            left_prefix_sum += nums[i]
            right_prefix_sum -= nums[i]

            if left_prefix_sum >= right_prefix_sum:
                res += 1
        
        return res
