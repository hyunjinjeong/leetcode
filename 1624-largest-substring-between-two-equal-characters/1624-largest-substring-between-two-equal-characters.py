class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # 각 캐릭터마다 최초 포지션을 기록하면 될 듯?
        first_pos = {}

        ans = -1
        for i in range(len(s)):
            if s[i] in first_pos:
                ans = max(i - first_pos[s[i]] - 1, ans)
            else:
                first_pos[s[i]] = i

        return ans