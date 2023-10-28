class DetectSquares:
    # x 포인트, y 포인트로 각각 dict 관리?
    # 그럼 square를 찾으려면 x에서 찾고 y에서 찾고... 
    # 만약 하나에서 찾으면 square니까 길이가 동일한.. 예를 들어 (i, j)에서 시작하면
    # (i, z)란게 있으면 다음에 y가 (j - z)에 있는지 찾아야 하고 그 다음에는 반대쪽 모서리...

    def __init__(self):
        self.counter = collections.defaultdict(int)
        self.x_pos = collections.defaultdict(list)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.counter[(x, y)] += 1
        self.x_pos[x].append(y)

    def count(self, point: List[int]) -> int:
        x, y1 = point
        # x나 y 중 하나만 보면 되지 않나..? x 먼저 보면.
        ans = 0
        for y2 in self.x_pos[x]:
            length = abs(y1 - y2)
            if length == 0:
                continue
            
            # 점 2개 나왔고, 길이가 있으니 나머지 점 2개를 그냥 체크하면 됨. 경우의 수는 두가지
            ans += self.counter[(x-length, y1)] * self.counter[(x-length, y2)]
            ans += self.counter[(x+length, y1)] * self.counter[(x+length, y2)]
            
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)