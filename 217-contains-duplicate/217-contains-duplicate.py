class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 간단하게 이것도 되겠는뎅
        return len(nums) != len(set(nums))