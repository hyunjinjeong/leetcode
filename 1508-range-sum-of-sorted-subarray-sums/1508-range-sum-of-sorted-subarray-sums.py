class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # ?? 직접 만드는거 말고 다른 방법이 있나
        MOD = 10 ** 9 + 7

        subarray_sum = []
        for i in range(len(nums)):
            curr = 0
            for j in range(i, len(nums)):
                curr += nums[j]
                subarray_sum.append(curr)
        
        subarray_sum.sort()
        
        res = 0
        for i in range(left - 1, right):
            res = (res + subarray_sum[i]) % MOD
        return res
