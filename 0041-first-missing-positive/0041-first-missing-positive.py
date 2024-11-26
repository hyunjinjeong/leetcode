class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # non-constant space면.. set을 만들어서 다 넣고
        # 1부터 len(nums)까지 존재하는지 확인
        # 이거를 constant space로 하려면..
        num_set = set(nums)
        for num in range(1, len(nums) + 1):
            if num not in num_set:
                return num
        
        return len(nums) + 1