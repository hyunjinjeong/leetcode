class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 요것도 xor 쓰는거 같은디
        # 0-n까지 한번씩 xor 돌려놓고 다시 nums랑 돌리면
        # 나머지는 2번씩 해서 0이 되고 없는 것만 1번이라서 남음

        ans = 0
        for num in range(0, len(nums) + 1):
            ans ^= num

        for num in nums:
            ans ^= num
        
        return ans
            