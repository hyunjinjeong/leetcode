class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # subarray sum equals k랑 똑같은 문제
        res = 0

        acc_sum = collections.defaultdict(int)
        curr_sum = 0

        for num in nums:
            curr_sum += num
            if curr_sum == goal:
                res += 1
            if curr_sum - goal in acc_sum:
                res += acc_sum[curr_sum - goal]
            
            acc_sum[curr_sum] += 1
        
        return res