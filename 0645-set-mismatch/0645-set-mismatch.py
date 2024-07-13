class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # 일단 이렇게 하면 됨
        ans = []
        seen = set()
        for num in nums:
            if num in seen:
                ans.append(num)
            else:
                seen.add(num)
        
        for num in range(1, len(nums) + 1):
            if num not in seen:
                ans.append(num)
        
        return ans