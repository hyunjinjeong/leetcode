class Solution:
    def partitionString(self, s: str) -> int:
        ans = 1
        last_index = {}

        left = 0
        for right, c in enumerate(s):
            if last_index.get(c, -1) >= left:
                left = right
                ans += 1
            last_index[c] = right
        
        return ans