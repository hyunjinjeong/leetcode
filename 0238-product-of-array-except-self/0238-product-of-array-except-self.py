class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)

        prefix_product = [1] * (N + 1)
        for i in range(1, N + 1):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
        
        suffix_product = [1] * (N + 1)
        for i in range(len(nums) - 1, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i]
        
        res = [1] * N
        for i in range(N):
            res[i] = prefix_product[i] * suffix_product[i + 1]
        
        return res