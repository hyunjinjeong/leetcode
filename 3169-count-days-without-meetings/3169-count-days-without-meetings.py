class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # overlapping intervals 문제구만
        # 구하고 나면? 돌면서 days에서 각 인터벌 범위만큼 빼주면 될 듯

        meetings.sort()
        
        prev_start, prev_end = meetings[0]
        new_meetings = [[prev_start, prev_end]]

        for i in range(1, len(meetings)):
            start, end = meetings[i]
            prev_start, prev_end = new_meetings[-1]

            if start <= prev_end:
                new_meetings[-1][1] = max(end, prev_end)
            else:
                new_meetings.append([start, end])

        res = days
        for start, end in new_meetings:
            res -= end - start + 1
        return res
