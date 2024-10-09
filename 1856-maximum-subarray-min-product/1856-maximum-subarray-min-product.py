class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        # brute force는 subarray를 다 구해서 계산하는 거일거고..
        # greedy는 안 될 것 같음. DP이려나..? 근데 min이 매번 달라질 수 있는데 어떻게 sub problem을 활용하지...


        # 일단 sum을 구하는건 prefix sum을 미리 계산해두면 O(1)으로 된다.
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        # 그럼 여기서 min(subarray) * sum을 구하는 건? 얘는 O(n)이 드는데
        # 아 minimum을 monotonic stack을 이용해서 구할 수 있당
        res = 0
        stack = []
        for i, num in enumerate(nums + [0]):
            while stack and nums[stack[-1]] >= num:
                curr_min = nums[stack.pop()]
                left = stack[-1] if stack else -1
                res = max(res, curr_min * (prefix_sum[i] - prefix_sum[left + 1]))
            stack.append(i)
        
        return res % (10**9 + 7)