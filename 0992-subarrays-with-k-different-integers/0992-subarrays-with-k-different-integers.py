class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # k == atMost(k) - atMost(k - 1) 이구나

        def at_most(target):
            res = 0
            
            count = {}
            left = 0
            for right in range(len(nums)):
                count[nums[right]] = count.get(nums[right], 0) + 1

                while len(count) > target:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1

                res += right - left + 1
            
            return res

        return at_most(k) - at_most(k - 1)