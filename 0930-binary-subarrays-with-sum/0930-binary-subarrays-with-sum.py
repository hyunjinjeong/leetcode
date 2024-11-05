class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # # subarray sum equals k랑 똑같은 문제
        # res = 0

        # acc_sum = collections.defaultdict(int)
        # curr_sum = 0

        # for num in nums:
        #     curr_sum += num
        #     if curr_sum == goal:
        #         res += 1
        #     if curr_sum - goal in acc_sum:
        #         res += acc_sum[curr_sum - goal]
            
        #     acc_sum[curr_sum] += 1
        
        # return res
        # sliding window로 풀어보자
        def at_most(num):
            if num < 0:
                return 0
            
            res, left = 0, 0
            curr_sum = 0
            for right in range(len(nums)):
                curr_sum += nums[right]
                while curr_sum > num:
                    curr_sum -= nums[left]
                    left += 1
                res += right - left + 1
            return res
        
        return at_most(goal) - at_most(goal - 1)


