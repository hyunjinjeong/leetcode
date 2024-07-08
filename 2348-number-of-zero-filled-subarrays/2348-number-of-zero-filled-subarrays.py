class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # 길이가 n일 때 1~n까지의 합이라고 봐도 되겠네. 그러면 n(n+1) // 2
        ans = 0
        zero_length = 0

        for num in nums + [1]:
            if num == 0:
                zero_length += 1
            else:
                ans += (zero_length) * (zero_length + 1) // 2
                zero_length = 0
        
        return ans