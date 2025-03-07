class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # 동일 선상에 있는 점들..? y = ax + b에서 a와 b가 같아야 함
        # 특정 한 점에서 다른 모든 점에 대해서 같은 선상인지 구할 수 있음
        # 모든 점에 대해서 확인하면 되지 않나? 최대 300개라 괜찮을 듯
        # 특정 점에 대해서는 기울기만 같으면 됨.

        res = 1
        for i in range(len(points)):
            slopes = collections.defaultdict(list)
            base_x, base_y = points[i]
            for j in range(len(points)):
                if i == j:
                    continue
                target_x, target_y = points[j]
                if target_y != base_y:
                    slope = (target_x - base_x) / (target_y - base_y)
                else:
                    slope = None
                
                slopes[slope].append(j)
                res = max(len(slopes[slope]) + 1, res)
        
        return res