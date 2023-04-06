class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 아.. prefix sum이 k만큼 증가하면 count.
        # 1 1 1 -2 1의 경우 0 1 2 3 1 2 가 될 테니까 0->2, 1->3, 0->2 (처음, 끝)
        # 즉 count를 저장하고 prefix_sum - k가 dict에 있는지 보면 됨.
        
        ans = 0
        prefix_sum = 0
        count = {0:1}
        
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in count:
                ans += count[prefix_sum - k]
            
            count[prefix_sum] = count.get(prefix_sum, 0) + 1    
        
        return ans