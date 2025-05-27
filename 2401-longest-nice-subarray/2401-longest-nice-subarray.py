class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # sliding window 같음
        # and 값을 저장하고 0이 깨지면..? 다시 0이 될 때까지 left를 줄임. 그리고 res 갱신.
        # 근데 left += 1을 할 때 무슨 연산을 해야 하는 걸까
        longest = 1
        curr_or = nums[0]

        left = 0
        for right in range(len(nums)):
            while left < right and curr_or & nums[right] != 0:
                curr_or ^= nums[left] # 중복된 비트가 없기 때문에, nums[left]의 비트를 지우는 연산이 됨
                left += 1
            
            curr_or |= nums[right]
            longest = max(longest, right - left + 1)

        return longest
