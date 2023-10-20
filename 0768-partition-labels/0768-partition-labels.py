class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # greedy...
        last = {c:i for i, c in enumerate(s)}

        ans = []

        left, right = 0, 0
        for i, c in enumerate(s):
            right = max(right, last[c])

            if i == right:
                ans.append(right - left + 1) # 구간 갯수
                left = right + 1

        return ans