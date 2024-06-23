class Solution:
    def specialArray(self, nums: List[int]) -> int:
        N = len(nums)
        
        # counting sort..!
        freq = [0] * (N + 1)
        for num in nums:
            freq[min(num, N)] += 1
        
        nums_greater_than_equal = 0
        for i in range(N, 0, -1):
            nums_greater_than_equal += freq[i]
            if i == nums_greater_than_equal:
                return i
        
        return -1
            