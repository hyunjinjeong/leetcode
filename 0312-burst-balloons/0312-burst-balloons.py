class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # i번째에서 터트릴지 or 안 터트릴지.
        # 근데 이전에 뭘 터트렸는지를 알아야 함.
        # dfs + cache?

        # def dfs(coin, curr):
        #     if not curr:
        #         return coin
            
        #     ans = 0
        #     for i in range(len(curr)):
        #         prev = curr[i - 1] if i > 0 else 1
        #         nxt = curr[i + 1] if i < len(curr) - 1 else 1
        #         ans = max(dfs(coin + prev * curr[i] * nxt, curr[:i] + curr[i+1:]), ans)

        #     return ans

        cache = {}

        def dfs(left, right):
            if left > right:
                return 0
            if (left, right) in cache:
                return cache[(left, right)]
            
            ans = 0
            prev = nums[left - 1] if left > 0 else 1
            nxt = nums[right + 1] if right < len(nums) - 1 else 1
            for i in range(left, right + 1):
                coin = prev * nums[i] * nxt
                coin += dfs(left, i - 1) + dfs(i + 1, right)
                ans = max(coin, ans)

            cache[(left, right)] = ans
            return cache[(left, right)]
        
        return dfs(0, len(nums) - 1)
