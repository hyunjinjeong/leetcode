class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 더한게 음수이면 새로 시작..?
        ans = float("-inf")
        curr = 0
        for num in nums:
            curr += num
            ans = max(curr, ans)
            if curr < 0:
                curr = 0
        
        return ans