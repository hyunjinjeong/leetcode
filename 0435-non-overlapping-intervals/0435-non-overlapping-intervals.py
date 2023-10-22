class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[1])

        ans = 0

        last_end = float("-inf")
        for i in intervals:
            if last_end > i[0]:
                ans += 1
            else:
                last_end = i[1]

        return ans
        