class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 중복 인터벌을 다 합치는 문제는 아니네.. 그러면 문제 정의가 흠
        # 뭔가 중복된 인터벌을 처리하는 건 맞는데...
        # 그럼 다시 1 8 / 2 6 / 7 12 / 10 16 예시로 가보면
        # 2 6 / 1 8 / 7 12 / 10 16 에서
        
        # start로 정렬을 하면?
        # 1 8 / 2 6 / 7 12 / 10 16

        # 겹치는 부분만 남겨볼까?
        # 1 6이 되고 / 새로 시작해서 10 12가 될거임
        # 그럼 2개고

        # 1 2 / 2 3 / 3 4 / 4 5 는
        # 2 2 / 4 4 -> 2개.
        # 이거 말이 되는데?

        # 그럼 겹치는 부분은 어떻게 구하지? start나 end 둘 중 하나로 정렬을 해야 하는데
        # start로 정렬이 말이 될 것 같음
        # start로 정렬한 다음에
        # curr가 있으면, curr[end] >= point[start] 이면 겹치는거
        # 겹친다고 판정이 되면, 범위는 [point[start], min(curr[end], point[end])]
        # 이렇게 하나 넣고, 다음에 또 현재 curr에 대해서 하면 될 듯?
        # 1 8 / 2 6 / 3 7 / 7 12 이라면
        # 2 6이 됨. 그 다음 3 6이 됨
        # 그러면 3 6에서 7 12가 되니까 이건 그냥 넘어가고
        # 7 12 에서 10 16은 10 12가 되고.
        START, END = 0, 1
        points.sort(key=lambda point: point[START])
        points.append([float("inf"), float("inf")])

        overwrapping_points = []
        curr_start, curr_end = points[0]
        for i in range(1, len(points)):
            point_start, point_end = points[i]
            if point_start <= curr_end:
                curr_start, curr_end = point_start, min(curr_end, point_end)
            else:
                overwrapping_points.append([curr_start, curr_end])
                curr_start, curr_end = points[i]

        return len(overwrapping_points)