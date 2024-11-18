class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # N = len(nums)
        # prefix_sum = [0] * (N + 1)
        # for i in range(1, N + 1):
        #     prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        
        # @cache
        # def dfs(start, part):
        #     if part == k:
        #         return prefix_sum[N] - prefix_sum[start]

        #     res = float("inf")
        #     for i in range(start, N - (k - part)):
        #         curr = prefix_sum[i + 1] - prefix_sum[start]
        #         rest = dfs(i + 1, part + 1)

        #         res = min(res, max(curr, rest))
        
        #     return res

        # return dfs(0, 1)

        # binary search works...!
        def satisfy(target_sum):
            curr_part, curr_sum = 1, 0
            for num in nums:
                if num > target_sum:
                    return False
                
                if curr_sum + num > target_sum:
                    curr_part += 1
                    curr_sum = num
                else:
                    curr_sum += num
                
                if curr_part > k:
                    return False
            
            return True

        total_sum = sum(nums)
        lo, hi = 0, total_sum

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if satisfy(mid):
                hi = mid
            else:
                lo = mid + 1
        
        return lo