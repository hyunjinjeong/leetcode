class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # xor 하면 됨
        ans = 0

        for num in nums:
            ans ^= num
        
        return ans