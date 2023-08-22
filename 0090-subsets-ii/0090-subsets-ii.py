class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 중복 검사를 위해 sort
        nums.sort()
        return self.backtrack(0, [], nums, [])
    
    def backtrack(self, start, curr, nums, ans):
        ans.append(curr[:])

        for i in range(start, len(nums)):
            # 중복은 거르기
            # [2, 2] 같은 경우를 해결하기 위해 i > start 조건 추가.
            if i > start and nums[i] == nums[i-1]:
                continue

            curr.append(nums[i])
            self.backtrack(i + 1, curr, nums, ans)
            curr.pop()

        return ans