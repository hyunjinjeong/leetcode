class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # y값은 필요 없고 x값만 있으면 됨. 그리고 제일 긴 interval을 고르면 될 듯?
        points.sort(key=lambda point: point[0])

        res = 0
        for i in range(1, len(points)):
            res = max(res, points[i][0] - points[i-1][0])
        
        return res