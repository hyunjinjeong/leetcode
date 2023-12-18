class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = collections.defaultdict(int)

        for i in range(len(wall)):
            acc_length = 0
            for j in range(len(wall[i]) - 1): # col 개수가 모두 다름 + 마지막 edge는 제외
                acc_length += wall[i][j]
                edges[acc_length] += 1

        # height - max(edges)
        return len(wall) - max(edges.values(), default=0)