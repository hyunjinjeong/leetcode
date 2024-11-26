class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # non-constant space면.. set을 만들어서 다 넣고
        # 1부터 len(nums)까지 존재하는지 확인
        # 이거를 constant space로 하려면..
        # num이 1 ~ len(nums)까지라는게 중요하구나... in-place로 마킹하면 됨
        N = len(nums)
        for i in range(N):
            num = nums[i]
            if num > 2**31:
                num = num - 2**32

            if 1 <= num <= N and nums[num - 1] <= 2**31:
                nums[num - 1] = 2**32 + nums[num - 1]
        
        for i in range(N):
            num = nums[i]
            if num <= 2**31:
                return i + 1
        
        return N + 1