class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 음 그래프 문제 아닌가?
        # 쭉 돌면서 adjacent cell에 edge 연결하고
        # 벨만 포드 돌리기?
        # DP 비슷할 것 같기도 한데 왜냐면 row 단위로는 sub problem에 속함
        dp = [0] * (len(triangle) + 1)

        # 0 -> 0 1
        # 1 -> 1 2
        # 2 -> 2 3 ..
        # 0 1 2 면 0은 0, 1은 0 1, 2는 1 2
        # 그럼 반대로 다음 row에서는 0 1이 0.. 즉 dp[i] + min(row[i], row[i + 1])
        # reverse로 도는게 편하겠다.

        for row in range(len(triangle) - 1, -1, -1):
            new_dp = [0] * len(triangle)
            for i in range(len(triangle[row])):
                new_dp[i] = triangle[row][i] + min(dp[i], dp[i + 1])
            dp = new_dp
        
        return dp[0]