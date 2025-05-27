class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # sliding window 같음
        # and 값을 저장하고 0이 깨지면..? 다시 0이 될 때까지 left를 줄임. 그리고 res 갱신.
        # 근데 left += 1을 할 때 무슨 연산을 해야 하는 걸까
        # bit 단위로 보면 1이랑 0이 있을건데
        # 0이 깨졌다는 건 nums[right]랑 nums[left]에 1이 겹치는 비트가 있다는 뜻
        # 그러면 nums[left], nums[left + 1], .. 오면서 연산으로 알 방법이 없지 않나?
        # 그러면 비트별로 1 카운트를 세기? 비트 하나당 카운트가 2 이상이면 조건이 깨지는 거임.
        longest = 1
        curr_and = nums[0]

        left = 0
        for right in range(len(nums)):
            while left < right and curr_and & nums[right] != 0:
                curr_and ^= nums[left]
                left += 1
            
            curr_and |= nums[right]
            longest = max(longest, right - left + 1)

        return longest
