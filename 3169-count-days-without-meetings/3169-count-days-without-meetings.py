class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # overlapping intervals 문제구만
        # 구하고 나면? 돌면서 days에서 각 인터벌 범위만큼 빼주면 될 듯

        meetings.sort()
        prev_start, prev_end = meetings[0]
        res = days

        for start, end in meetings:
            if start <= prev_end:
                prev_end = max(end, prev_end)
            else:
                res -= prev_end - prev_start + 1
                prev_start, prev_end = start, end
        
        res -= prev_end - prev_start + 1
        return res
