class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 아 이렇게 풀 수도 있음.
        # end로 정렬해서, point[start] > curr[end]면 하나씩 늘려줄 수 있음.
        res = 1

        START, END = 0, 1
        points.sort(key=lambda point: point[END])

        curr_end = points[0][END]
        for i, point in enumerate(points, start=1):
            if point[START] > curr_end:
                res += 1
                curr_end = point[END]

        return res
