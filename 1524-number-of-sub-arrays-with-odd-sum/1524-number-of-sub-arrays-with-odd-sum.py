class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # 투포인터? DP?
        # 슬라이딩 윈도우는 윈도우가 언제 늘고 줄어날지 몰라서 아님. DP도 뭔가 애매함.
        # 구간합은 prefix sum을 구해둬야 하나? 짝수인지 아닌지만 알면 되긴 하는데
        MOD = 10 ** 9 + 7

        res = 0

        prefix_sum = 0
        odd_sum, even_sum = 0, 1
        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 == 1:
                res += even_sum
                odd_sum += 1
            else:
                res += odd_sum
                even_sum += 1
            
            res %= MOD
        
        return res
