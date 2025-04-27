class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # 홀수를 1 짝수를 0으로 바꾸면 알고 있는 문제임...
        prefix_sum = 0
        count = {}

        res = 0
        for num in nums:
            prefix_sum += num & 1
            if prefix_sum == k:
                res += 1
            if prefix_sum - k in count:
                res += count[prefix_sum - k]
            
            count[prefix_sum] = count.get(prefix_sum, 0) + 1
        
        return res
