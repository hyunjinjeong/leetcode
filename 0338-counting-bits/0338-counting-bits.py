class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(1, n+1):
            # 짝수면 >> 1 한거 그대로고
            # 홀수면 >> 1 한거에 +1 하면 되지 않나?
            if i & 1:
                ans[i] = ans[i >> 1] + 1
            else:
                ans[i] = ans[i >> 1]
        
        return ans