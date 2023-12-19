class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        
        prefix_sum = 0
        count = {}
        for num in nums:
            prefix_sum += num
            if prefix_sum == k:
                ans += 1
            if prefix_sum - k in count:
                ans += count[prefix_sum - k]
            
            count[prefix_sum] = count.get(prefix_sum, 0) + 1
        
        return ans