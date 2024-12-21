class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # nums[i]를 지우면 값이 nums[i] - 1, nums[i] + 1인 모든 원소를 지워야 함
        # 그러면 nums[i]가 크면 클수록 좋고 또 갯수가 많으면 좋을 듯?
        # dp를 적용할 수 있으려나? 2 2 3 3 3 4에서 3을 하나 지우면 2 2 4가 다 지워짐
        # 각 숫자에 대해서 생각해보자. 그러면 nums[i]를 지우면 얻을 수 있는 값은 count[nums[i]] * nums[i]임
        # 대신 기회비용으로 손해보는 값이 생기고...
        # pick & not pick으로 가능하려나? count만 미리 계산해두면 될 듯?
        
        count = collections.Counter(nums)
        min_num, max_num = min(nums), max(nums)

        @cache
        def dfs(num):
            if num > max_num:
                return 0
            
            pick = count[num] * num + dfs(num + 2)
            not_pick = dfs(num + 1)
            return max(pick, not_pick)
        
        return dfs(min_num)