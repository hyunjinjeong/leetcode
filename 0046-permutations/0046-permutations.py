class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.backtrack([], nums, set())
        return self.ans

    def backtrack(self, curr, nums, visited):
        if len(curr) == len(nums):
            self.ans.append(curr[:])
            return

        for num in nums:
            if num in visited:
                continue

            visited.add(num)
            curr.append(num)
            self.backtrack(curr, nums, visited)
            curr.pop()
            visited.remove(num)