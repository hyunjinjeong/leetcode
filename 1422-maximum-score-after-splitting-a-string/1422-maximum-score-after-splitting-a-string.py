class Solution:
    def maxScore(self, s: str) -> int:
        # 그냥 쭉 돌면서 max 세면 될 듯?
        left = 1 if s[0] == "0" else 0
        right = 0

        for i in range(1, len(s)):
            if s[i] == "1":
                right += 1

        ans = left + right
        for i in range(1, len(s) - 1):
            if s[i] == "1":
                if right > 0: right -= 1
            else:
                left += 1
            ans = max(left + right, ans)

        return ans