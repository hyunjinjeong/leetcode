class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # 어떤 color를 골라야 하는가? 이건 명확함. 연속해서 동일한 컬러가 나오지 않도록.
        # 그럼 최소를 만드려면? 연속된 N개 중 낮은 순으로 N - 1개를 고르면 됨.
        # 그리고 한 group을 제거해도 최소 1개는 남기 때문에 연쇄적으로 합쳐지지는 않음. 개별로 신경쓰면 된다..
        # one pass로도 될 거 같기도 한데?
        # curr_max랑 sum을 구하면서
        # 같은 색깔이 끝나면 sum - curr_max를 결과에다가 더해주면 될 듯

        # 1 2 <- sum 3. curr_max 2
        # 2 3 에서 끝나니까 결과에 1 더해주고.
        # 3 4 -> sum 5 curr_max 4. 이것도 결과에 1 더해주고
        # 그럼 2.
        res = 0

        curr_color, curr_max, curr_sum = colors[0], neededTime[0], neededTime[0]
        for i in range(1, len(colors)):
            color, time = colors[i], neededTime[i]
            if color == curr_color:
                curr_sum += time
                curr_max = max(curr_max, time)
            else:
                res += curr_sum - curr_max
                curr_color, curr_max, curr_sum = color, time, time
        
        # 마지막 계산
        if curr_sum > neededTime[-1]:
            res += curr_sum - curr_max

        return res