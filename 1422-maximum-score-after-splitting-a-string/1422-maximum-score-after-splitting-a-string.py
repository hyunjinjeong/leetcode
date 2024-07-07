class Solution:
    def maxScore(self, s: str) -> int:
        zeros, ones = 0, s.count("1")
        ans = 0

        for i in range(len(s) - 1):
            if s[i] == "1":
                ones -= 1
            else:
                zeros += 1
            ans = max(ones + zeros, ans)

        return ans