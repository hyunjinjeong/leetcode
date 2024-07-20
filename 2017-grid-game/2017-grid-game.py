class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # 한번 r=1로 내려가면 다시 올라갈 수 없음. 거기서부터는 정해진 경로
        # 즉 첫번째 로봇의 경우의 수는 n개임
        # dp는 안된다.. 왜냐면 robot 1 최댓값을 구해도 그게 답이 아님

        # Hint: prefix sum?
        # first row, second row 각각 prefix sum을 구해두면
        # prefix sum 방향은 first row는 left -> right, second는 right -> left
        # 그러면 first_row_sum[0] + second_row_sum[0]
        # first_row_sum[1] + second_row_sum[1] 이런 식으로 O(1)에 구할 수 있다.

        # 여기서 robot 2는 어떻게 하냐...
        # robot 1이 지나간 경로는 다 쓸고 가니까...
        # first row에서 맨 끝까지 가서 내려가거나, 바로 내려가는 두 가지 경우의 수밖에 없는 듯?
        # 두 개 max는 O(1)이니까 N개에 대해서 구하면 될 것 같다


        N = len(grid[0])

        first_row_sum, second_row_sum = [grid[0][0]], [grid[1][N-1]]
        for i in range(1, N):
            first_row_sum.append(first_row_sum[i-1] + grid[0][i])
            second_row_sum.append(second_row_sum[i-1] + grid[1][N-1-i])
        second_row_sum.reverse()
        
        ans = float("inf")
        for i in range(N):
            second_robot_points = max(first_row_sum[N-1] - first_row_sum[i], second_row_sum[0] - second_row_sum[i])
            print(second_robot_points)
            ans = min(second_robot_points, ans)
        
        return ans