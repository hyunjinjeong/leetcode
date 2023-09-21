class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp
        # 곱하기라서 max min 둘다 관리..
        tmp_max, tmp_min = 1, 1
        ans = float("-inf")

        for num in nums:
            product_from_max = tmp_max * num
            product_from_min = tmp_min * num
            
            tmp_max = max(product_from_max, product_from_min, num)
            tmp_min = min(product_from_max, product_from_min, num)

            ans = max(tmp_max, ans)
        
        return ans