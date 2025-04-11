class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0

        curr_sum = 0
        counter = collections.defaultdict(int)

        left = 0
        for right in range(len(nums)):
            if right - left + 1 > k:
                curr_sum -= nums[left]
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1
            
            curr_sum += nums[right]
            counter[nums[right]] += 1
            if len(counter) == k:
                res = max(curr_sum, res)
        
        return res
