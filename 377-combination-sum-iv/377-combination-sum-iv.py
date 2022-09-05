class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 일단 생각해보면
        # target이 nums[i]보다 작으면 안되고.
        
        # dp[n]를 값이 n일 때의 조합 갯수라고 하면
        # nums를 다 돌면서 이걸 계산하면 되지 않으려나?
        # dp[i] += dp[i-num]
        
        dp = [0] * (target+1)
        
        for i in range(1, target+1):
            for num in nums:
                if i < num:
                    continue
                elif i == num:
                    dp[i] += 1
                elif i >= num:
                    dp[i] += dp[i-num]
            
        return dp[-1]