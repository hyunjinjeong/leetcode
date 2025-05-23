class Solution:
    def minChanges(self, s: str) -> int:
        # greedy 하게 처리가 가능할 것 같은디
        # 00 11이면 필요 없고 10, 01이면 1개씩 바꾸면 되니까.. 그냥 2개씩 돌면서 10이나 01이면 1씩 더하면 될 듯?
        ans = 0

        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                ans += 1
        
        return ans
