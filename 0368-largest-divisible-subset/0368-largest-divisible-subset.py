class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # 최소공배수를 유지하면서 하나씩 추가해가면 길이는 나올 것 같은데.. 리스트 자체는 어떻게 구하지
        # 생각해보니 하나씩 다 비교할 필요 없이 바로 이전 숫자랑만 비교하면 되지 않나? LIS구나
        N = len(nums)
        nums.sort()

        dp = [1] * N

        for i in range(N):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[j] + 1, dp[i])
        
        max_dp, max_index = 0, 0
        for i in range(N):
            if dp[i] > max_dp:
                max_dp, max_index = dp[i], i
        
        max_val = nums[max_index]

        res = []
        while max_index >= 0:
            if max_val % nums[max_index] == 0:
                res.append(nums[max_index])
            max_index -= 1
        res.reverse()
        
        return res